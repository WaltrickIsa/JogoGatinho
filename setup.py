import cx_Freeze
executaveis = [
    cx_Freeze.Executable(script="main.py", icon ="recursos/icone.ico")]
cx_Freeze.setup(
    nome = "Gatinho",
    options = {"build_exe":{
        "packages":["pygame"],
        "include files":["recursos"]
    }

    }, executables = executaveis
    
)

