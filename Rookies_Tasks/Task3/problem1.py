def spit_out(layers: int, is_hate: bool):
    if layers == 1:
        return 'it'

    if is_hate:
        return 'that I love ' + spit_out(layers-1, not is_hate)
    else:
        return 'that I hate ' + spit_out(layers-1, not is_hate)


print('I hate '+spit_out(int(input()), True))

