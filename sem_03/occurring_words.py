"""
2. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
Не учитывать знаки препинания и регистр символов. 
За основу возьмите любую статью из википедии или из документации к языку.
(Может помочь метод translate из модуля string)
"""

text = 'The pydoc module automatically generates documentation from Python modules. \
The documentation can be presented as pages of text on the console, \
served to a web browser, or saved to HTML files.\
For modules, classes, functions and methods, \
the displayed documentation is derived from the docstring (i.e. the __doc__ attribute) of the object,\
 and recursively of its documentable members. \
 If there is no docstring, pydoc tries to obtain a description from \
 the block of comment lines just above the definition of the class, function or method in the source file, \
 or at the top of the module (see inspect.getcomments()). \
 The built-in function help() invokes the online help system in the interactive interpreter, \
 which uses pydoc to generate its documentation as text on the console. \
 The same text documentation can also be viewed from outside the \
 Python interpreter by running pydoc as a script at the operating system’s command prompt. \
 For example, running python -m pydoc sys at a shell prompt will display documentation on the sys module, \
 in a style similar to the manual pages shown by the Unix man command. \
 The argument to pydoc can be the name of a function, module, or package, \
 or a dotted reference to a class, method, or function within a module or module in a package. \
 If the argument to pydoc looks like a path (that is, it contains the path separator for your operating system, \
 such as a slash in Unix), and refers to an existing Python source file, \
 then documentation is produced for that file.'

text = text.translate(str.maketrans({'.': '', ',': ''})).lower().split()
print(f'Длина текста составляет {len(text)} слов.')
frequent_words = {x: text.count(x) for x in text}
words = []
frequence = []

for key, value in frequent_words.items():
    words.append(key)
    frequence.append(value)

frequent_words = {}

for _ in range(10):
    max_frequence_index = frequence.index(max(frequence))
    frequent_words[words[max_frequence_index]] = max(frequence)
    words.pop(max_frequence_index)
    frequence.pop(max_frequence_index)

print(f'10 самых часто встречающихся слов: ')
for key, value in frequent_words.items():
    print(f'Слово "{key}" - частота повторений - {value}')
