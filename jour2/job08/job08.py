def flseason(type,saison):
    match type,saison:
        case 'fruits','hiver':
            result=print("orange, mandarine et kiwi")
        case 'fruits','ete':
            result=print("Poire, fraise, cassis")
        case 'legume', 'hiver':
            result=print("carotte, topinambour, endive")
        case 'legume', 'ete':
            result=print("artichaut, aubergine,navet")
    return result

flseason('fruits','hiver')
flseason('fruits','ete')
flseason('legume','hiver')
flseason('legume','ete')
    