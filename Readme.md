# PaperlessAutomation
This is my approach for automating [Paperless-ngx](https://docs.paperless-ngx.com/).

Goal is to use these as Post-Processing Scripts.

## Modules
There are two kinds of Modules: Helper and Automation

### Automation
Automation modules do the work.
They contain a `main.py` file which is the starting point for this module. And they use a YAML for 
configuration. The YAML is named like `module_name.yaml`.

#### TagsToCustomFields
[TagsToCustomFields](ttcf/Readme.md) automates the conversion from tags to values of a dropdown CustomField.

### Helper
Helper modules are not ment to be used on its own. They are supporting the Automation modules.

#### PaperlessAccess 
[PaperlessAccess](pla/Readme.md) provides the general access to paperless by using a yaml to configure the credentials.

## Dependencies

* [Paperless API](https://github.com/tb1337/paperless-api/tree/main) for Paperless access
* [PyYAML](https://pyyaml.org/) - for reading configuration files


This project is being developed under the terms of the Apache License, Version 2.0.