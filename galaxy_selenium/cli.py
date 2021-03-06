REMOTE_DESCRIPTION = "Use a remote driver for selenium connection."
BROWSER_DESCRIPTION = "Use specific browser for selenium (e.g. firefox or chrome)."
REMOTE_HOST_DESCRIPTION = "Selenium hub remote host to use (if remote driver in use)."
REMOTE_PORT_DESCRIPTION = "Selenium hub remote port to use (if remote driver in use)."
GALAXY_URL_DESCRIPTION = "URL of Galaxy instance to target."
HEADLESS_DESCRIPTION = "Use local selenium headlessly (requires pyvirtualdisplay)."

from six.moves.urllib.parse import urljoin

from .driver_factory import (
    get_local_driver,
    get_remote_driver,
    virtual_display_if_enabled,
)
from .navigates_galaxy import NavigatesGalaxy


def add_selenium_arguments(parser):
    """Add common selenium arguments for argparse driver utility."""

    parser.add_argument(
        '--selenium-browser',
        default="auto",
        help=BROWSER_DESCRIPTION,
    )
    parser.add_argument(
        '--selenium-headless',
        default=False,
        action="store_true",
        help=HEADLESS_DESCRIPTION,
    )
    parser.add_argument(
        '--selenium-remote',
        default=False,
        action="store_true",
        help=REMOTE_DESCRIPTION,
    )
    parser.add_argument(
        '--selenium-remote-host',
        default="127.0.0.1",
        help=REMOTE_HOST_DESCRIPTION,
    )
    parser.add_argument(
        '--selenium-remote-port',
        default="4444",
        help=REMOTE_PORT_DESCRIPTION,
    )
    parser.add_argument(
        '--galaxy-url',
        default="http://127.0.0.1:8080/",
        help=GALAXY_URL_DESCRIPTION,
    )

    return parser


def args_to_kwds(args):
    kwds = {
        'selenium_browser': args.selenium_browser,
        'selenium_headless': args.selenium_headless,
        'selenium_remote': args.selenium_remote,
        'host': args.selenium_remote_host,
        'port': args.selenium_remote_port,
        'galaxy_url': args.galaxy_url,
    }
    return kwds


class DriverWrapper(NavigatesGalaxy):

    """Adapt argparse command-line options to a concrete Selenium driver."""

    def __init__(self, args=None, **kwds):
        if args is not None:
            assert not kwds
            kwds = args_to_kwds(args)

        self.target_url = kwds["galaxy_url"]
        # TODO: Allow overriding this.
        self.target_url_from_selenium = self.target_url

        browser = kwds.get("selenium_browser", "auto")
        self.display = virtual_display_if_enabled(kwds.get("selenium_headless", False))
        if kwds.get("selenium_remote", False):
            driver = get_remote_driver(
                host=kwds["selenium_remote_host"],
                port=kwds["selenium_remote_port"],
                browser=browser,
            )
        else:
            driver = get_local_driver(
                browser=browser,
            )
        self.driver = driver

    def build_url(self, url="", for_selenium=False):
        if for_selenium:
            return urljoin(self.target_url_from_selenium, url)
        else:
            return urljoin(self.target_url, url)

    @property
    def default_timeout(self):
        return 15

    def finish(self):
        exception = None

        try:
            self.driver.close()
        except Exception as e:
            exception = e

        try:
            self.display.stop()
        except Exception as e:
            exception = e

        if exception is not None:
            raise exception
