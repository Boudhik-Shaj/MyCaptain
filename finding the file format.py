#finding the file format

name = input("enter the file name with format: ")
StringLength = len(name) -1
ExtensionDictionary = {".scala":"scala",".py":"python",".cpp":"C++",".c":"C",".java":"java",".ipynb":"jupyter.notebook",".html":"html",".jl": "julia",".cr": "crystal",".ml": "ocaml",".exs": "elixir",".rkt": "racket",".scm": "csi -script",".ahk": "autohotkey",".au3": "autoit3",".kts": "kotlinc -script",".dart": "dart",".hs": "runhaskell",".nim": "nim",".csproj": "dotnet run --project",".fsproj": "dotnet run --project",".lisp": "sbcl --script",".kit": "kitc --run",".v": "v run",".vsh": "v run",".sass": "sass --style expanded",".ring": "ring"} #copied from vscode extenion map
for i in range(StringLength,-1,-1):
    if name[i] ==".":
        l= len(name) - i
        ExtensionString = name[-l:]
        print("file extension is ",ExtensionDictionary[str(ExtensionString)])