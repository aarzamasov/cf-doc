# cf-doc
Creating markdown descriprtion for cloudformation templates

# desclaimer
the script need a json file to create a description.

convert Yaml template with [cfn-flip](https://github.com/awslabs/aws-cfn-template-flip) to Json

for eg:
```bash 
cfn-flip vpc.yaml vpc.json
```

the script has no attributes this time.
but you can change the script for set them.

you can set:
- path to Json file
- type of markdown: classic or confluence

```python
a = GetMarkdown('/tmp/test/test.json', 'confluence')
```

# start the script
Type in your terminal
``` bash
python cf-doc.py
```