# PaperlessAutomation
This is my approach for automating [Paperless-ngx](https://docs.paperless-ngx.com/).

Goal is to use these as Post-Processing Scripts.

## post consumption configuration
Use `post_consumption.sh` as post conumption script.

i.e.: `/etc/paperless.conf`
```
...
PAPERLESS_PRE_CONSUME_SCRIPT="/var/opt/PaperlessAutomation/post_consumption.sh"
...
```
[paperless documentation](https://docs.paperless-ngx.com/advanced_usage/#post-consume-script)

## Launcher
### Configuration
The file `launcher.yaml` contains the configuration for the Post-Consumption script:
```
credentials:
  url: "<YOUR PAPERLESS URL>"
  api_token: "<YOUR TOKEN>"
postconsumption:
  - <LIST OF MODULES>
  - ttcf
```

### Usage
Just start the `main.py` File with a `launcher.yaml` config file right next to it.

## Modules
There are two kinds of Modules: Helper and Automation

### Automation
Automation modules do the work.
They contain a `main.py` file which is the starting point for this module. And they use a YAML for 
configuration. The YAML is named like `module_name.yaml`.

#### ttcf - TagsToCustomFields
[TagsToCustomFields](ttcf/Readme.md) automates the conversion from tags to values of a dropdown CustomField.

### Helper
Helper modules are not ment to be used on its own. They are supporting the Automation modules.

#### PaperlessAccess 
[PaperlessAccess](pla/Readme.md) provides the general access to paperless.

## Dependencies

* [Paperless API](https://github.com/tb1337/paperless-api/tree/main) for Paperless access
* [PyYAML](https://pyyaml.org/) - for reading configuration files


This project is being developed under the terms of the Apache License, Version 2.0.