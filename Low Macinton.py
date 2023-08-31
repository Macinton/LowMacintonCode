#from NSDT import scriptNSDT as scriptload
from sys import argv
from subprocess import call


commandsuses = []
commandswithargs = []
commandsbat = []

def argsposes(string, charneed):
    poses = []
    for i in range(len(string)):
        if string[i] == charneed: poses.append(i)
    return poses

def load(dirname):
    global commandsuses, commandsbat, commandswithargs
    #print(dirname[:-1])
    dirname += '\\'
    #print('')
    with open(dirname+'script.ilmp', 'r') as ac:
        for take in ac.readlines():
            splited = take.split(' : ')
            #print(splited[1][:-1])
            #construction(example): func : func.bat
            #                         0       1
            #append command with args(filepath)
            commandswithargs.append(dirname+splited[0])
            #append bat file(filepath)
            commandsbat.append(dirname+splited[1][:-1])
            #uses commands(not filepath)
            commandsuses.append(splited[0])
        #print(commandsbat)
        #print(commandswithargs)
        #print(commandsuses)

#argv.append('D:\\Low Macinton\\test.lms')
#print(argv[1])
#sleep(10)
if len(argv) == 2:
    head, tail = path.split(argv[1])
    batfile = 'compiled.bat'

    try:
        with open(argv[1], 'r') as rsf:
            strings = rsf.readlines()
            #print(strings)
           
    except:
        exit()

    else:
        try:
            with open(batfile, 'w') as mbf:
                mbf.write('@echo off\n')
            for take in strings:
                #print(take)
                splited = take.split(' : ')
                #print(splited[0] in commandsuses)
                if splited[0][-1] == '\n': splited[0] = splited[0][:-1]
                if splited[0] == 'USES':
                    #print(splited[1][:-1])
                    if splited[1][-1] == '\n': load(splited[1][:-1])
                    else: load(splited[1])

                else:
            
                    if splited[0] in commandsuses:
                        #with open(commandswithargs[commandsuses.index(splited[0])], 'r') as tce: commandexample = tce.readline()
                        #making bat(kill me please)
                        #print(batfile)
                        with open(batfile, 'a') as mbf:
                            inbat = commandsbat[commandsuses.index(splited[0])]
                            #print(inbat)
                            #inbat = inbat.replace('\n', '\\')
                            #print(inbat)
                            if inbat[-1] == '\n':
                                inbat = inbat[:-1]
                                #print(inbat)

                            with open(inbat.replace('\n', '\\'), 'r') as gbf:
                                batfilecommand = gbf.readlines()

                            #print(batfilecommand)
                            takeargs = 1
                            for takeb in batfilecommand:
                                #print(takeb)
                                #sleep(1)
                                
                                poses = argsposes(takeb, '~')
                                #print(poses)
                                takeb = list(takeb)
                                for numsargs in poses:
                                    takeb[numsargs] = splited[takeargs]
                                    #print(takeb[numsargs])
                                    takeargs += 1

                                outstring = ''
                                for takechar in takeb:
                                    outstring += takechar

                                mbf.write(outstring+'\n')
                                #print(outstring)





                    else:
                        if take[0] == '!' or take.replace(' ', '') == '':
                            pass

                        else:
                            print(2)
                            print(commandsuses)
                            exit()

            with open(batfile, 'a') as alc: alc.write('timeout /t 5 /nobreak >nul\n')
            call(batfile)

        except:
            print(1)
            exit()

else:
    #print(0)
    exit()
