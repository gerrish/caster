# new modules should be added in the dictionary
# the tupple contains the rules which will be imported

command_sets = {
    "bash.bash": ("Bash", ),
    "core.alphabet": ("Alphabet", ),
    "core.nav": ("Navigation", ),
    "core.numbers": ("Numbers", ),
    "core.punctuation": ("Punctuation", ),
    "cpp.cpp": ("CPP", ),
    "csharp.csharp": ("CSharp", ),
    "haxe.haxe": ("Haxe", ),
    "html.html": ("HTML", ),
    "java.java": ("Java", ),
    "javascript.javascript": ("Javascript", ),
    "python.python": ("Python", ),
    "rust.rust": ("Rust", ),
    "sql.sql": ("SQL", ),
    "prolog.prolog": ("Prolog", ),
    "vhdl.vhdl": ("VHDL", ),
}

for module_name, class_name_tup in command_sets.iteritems():
    for class_name in class_name_tup:
        try:
            _grammar = module_name.split(".")[1]
            _module = __import__(
                module_name, globals(), locals(),
                [_grammar])  #attempts to import the class  #attempts to import the class
            _class = getattr(_module, class_name)
            globals()[class_name] = _class  #make the name available globally

        except Exception as e:
            print("Ignoring ccr rule '{}'. Failed to load with: ".format(class_name))
            print(e)
