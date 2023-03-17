import glob
from typing import Any, Union

from js2py import EvalJs

script = ""
i: Union[Union[bytes, str], Any]
for i in glob.glob("C:/users/karuna/documents/*.js"):
    script += open(i, "r").read()
script = "for(var i=0;i<5;i++)document.write('hello world'+i)"
js = """
var output;
document = {
    write: function(value){
        output = value;
    }
}
""" + script

context = EvalJs()
context.execute(js)
print(context.output)
