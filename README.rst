A small library containing high level abstractions for driving Galaxy via Selenium.

* Free software: Academic Free License version 3.0
* Documentation: https://galaxy-selenium.readthedocs.org.
* Code: https://github.com/galaxyproject/galaxy-selenium

An Example
----------

The following example demonstrates the usage of this library by automating a few
tasks in Galaxy. This example will register a new user, upload this README via the
tool upload form, open the "Random Lines" tool, and execute it on the uploaded file.

::

    import os

    from random import randint

    from galaxy_selenium.cli import DriverWrapper

    driver_wrapper = DriverWrapper(galaxy_url="http://localhost:8080")

    driver_wrapper.register("mary%s@galaxyproject.org" % randint(0, 100000))
    driver_wrapper.perform_upload(os.path.abspath("./README.rst"))
    driver_wrapper.history_panel_wait_for_hid_ok(1)

    driver_wrapper.click_label("Text Manipulation")
    driver_wrapper.tool_open("random_lines1")
    driver_wrapper.tool_set_value("num_lines", "5")
    driver_wrapper.tool_execute()
    driver_wrapper.history_panel_wait_for_hid_ok(2)

    driver_wrapper.history_panel_click_item_title(hid=2)

    driver_wrapper.driver.save_screenshot("./randomlines.png")
