# python-selenium
Tutorial Selenium - curso dictado por Pablo Soifer 




#####Instalar selenium en tu proyecto
```python
pip install selenium
```

####Instalar Chrome Driver :
```json
https://chromedriver.chromium.org/downloads
```


####Como Lozalizar elementos:
```buildoutcfg
Id   (find_element_by_id)
Name (find_element_by_name)
Link Text (find_element_by_link_text)
Partial Link (find_element_by_partial_link_text)
Tag Name (find_element_by_tag_name)
Class Name (find_element_by_class_name)
CSS Selector (find_element_by_css_selector)
```

####Assert:
Assertions are simply boolean expressions that checks if
the conditions return true or not. If it is true, the 
program does nothing and move to the next line of code.
However, if it's false, the program stops and throws an error
