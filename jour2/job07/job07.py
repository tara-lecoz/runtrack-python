def whatlangage(langage):
    match langage:
        case 'javascript':
            print("tu es un developpeur web")
        case 'python':
            print("tu es un developpeur IA")
        case 'java':
            print("tu es un developpeur logiciel")
        case 'reactjs':
            print("tu es un developpeur mobile")
        case other:
            print("un jour, je serai le meilleur developpeur")
    return langage

whatlangage('javascript')
whatlangage('python')
whatlangage('java')
whatlangage('reactjs')
whatlangage('aucun')