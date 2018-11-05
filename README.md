# cf-doc
Creating markdown description from cloud formation templates

# disclaimer
the script works only with JSON files.

I fyou have YAML just convert it with [cfn-flip](https://github.com/awslabs/aws-cfn-template-flip) to Json

for eg:
```bash 
cfn-flip vpc.yaml vpc.json
```

The script has no attributes this time.
But you can change it into the script.

you can set:
- the path to JSON file
- type of markdown: classic or confluence

```python
a = GetMarkdown('/tmp/test/test.json', 'confluence')
```

# start the script
Type in your terminal
``` bash
python cf-doc.py
```

# example
You can find the example of a result of the script in `example` folder.
The markdown is for confluence article. For adding this two tables to confluence article you need to :
- push plus button
- find markup and click it
- chose confluence type 
- paste it into the filed of markdown
