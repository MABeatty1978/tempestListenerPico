# tempestListenerPicoW

This program is a basic server designed to run on a Raspberry Pi Pico W.  It scans a local network on port 50222 which is what the Tempest Weatherflow hub uses to broadcast UPD messages.  This is intended to be a framework to get started on larger projects.  When a weather observation, rain event, or lightning strike event happens, it'll grab the data from the event, format it, and display it to the debug console.

To use, edit the config.py file with your local SSID and network PASSWORD.  Then copy both .py files to your Raspberry Pi Pico W.
