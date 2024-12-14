# TagsToCustomField
Paperless cannot learn how to set CustomField Values automatically. If you have a dropdown or boolean 
custom field you can automate the assignment by using Tags and this script.

## Configuration

Searches for the CustomFields with ID `custom_field_id`, reads all options and puts the value.
All Tags are configured in `tags`. You can configure as many fields with as man tag-option pairs as 
you want.
```
fields:
  - custom_field_id: <your custom field id>
    type: [select|boolean]
    tags:
    - tag_id: <tag_id>
      option_value: [the option value|True|False]
```