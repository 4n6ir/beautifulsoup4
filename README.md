# beautifulsoup4

##### Cloud Development Kit (CDK) v2

```python
        region = Stack.of(self).region

        beautifulsoup4 = _lambda.LayerVersion.from_layer_version_arn(
            self, 'beautifulsoup4',
            layer_version_arn = 'arn:aws:lambda:'+region+':070176467818:layer:beautifulsoup4:3'
        )
```

##### AWS Lambda Layer for Python Library

 1. ```cd bundle```
 2. ```mkdir python```
 3. ```cd python```
 4. ```pip3 install beautifulsoup4 -t .```
 5. ```cd ..```
 6. ```zip -r beautifulsoup4.zip .```
 7. ```rm -R python```
 