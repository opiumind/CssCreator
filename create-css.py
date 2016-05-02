import sublime, sublime_plugin
import re


class CreateCssCommand(sublime_plugin.WindowCommand):
    def run(self):
        # gets current html file
        htmlFileName = self.window.active_view().file_name()

        if htmlFileName[-4:] == 'html':
            
            htmlFile = open(htmlFileName)

            classDeclarations = []
            cssSheet = ""

            for line in htmlFile:
                try:
                    # finds class attribute and remembers the beginning of its value
                    matchOfBegin = re.search('class=[\'|\"]{1}', line)
                    rawCoughtText = line[matchOfBegin.end():]

                    # counting indentation
                    try:
                        indentationMatch = re.search('^[\s]+', line)
                        lenOfIndentation = indentationMatch.end() - indentationMatch.start()
                    except:
                        lenOfIndentation = 0

                    # finds the end of class attribute value
                    matchOfEnd = re.search('[\'|\"]{1}', rawCoughtText)
                    rawClassNames = rawCoughtText[:matchOfEnd.start()]

                    # for the case if we have more than one class
                    try:
                        classNames = ''
                        classNamesList = rawClassNames.split()
                        for name in classNamesList:
                            classNames = classNames + '.' + name
                            classDeclarations.append((classNames, lenOfIndentation))
                    except:
                        continue

                except:
                    continue

            # if the first element with class has an indentation,
            # it will shift all indentations with this correction
            indentationCorrection = classDeclarations[0][1]

            # creates css skeleton with found classes
            for className, indentationsNum in classDeclarations:
                if indentationCorrection:
                    indentationsNum = indentationsNum - indentationCorrection
                cssSheet = cssSheet + ' ' * indentationsNum + className + ' ' + "{}\n"

            # creates a new file, sets css syntax highlight 
            # and writes created css skeleton
            newCssFile = self.window.new_file()
            newCssFile.set_syntax_file('Packages/CSS/CSS.tmLanguage')
            newCssFile.run_command("insert_snippet", {"contents": cssSheet})
