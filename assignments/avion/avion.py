import sys

def get_inputs():
    rows = []
    for i in range(5):
        row = input()
        rows.append(row)
    return rows
    
def main(rows):
    agent = ''
    for i, row in enumerate(rows):
        if 'FBI' in row:
            agent += f'{i+1} '
    
    if agent == '':
        agent = "HE GOT AWAY!"
    return agent

def testing():
    assert main(['E-FBIK','9A-TFGYU','K-UTDFU','G-ERRT','GIV-ETDYR']) == '1 '
    assert main(['ERT-FBITY','R-FFBI','59-SDFG','3ER-CVBN','FBI-WER']) == '1 2 5 '
    assert main(['','','','','']) == 'HE GOT AWAY!'
    print("All tests passed!", file=sys.stderr)


if __name__ == '__main__':
    testing()    
    print(main(get_inputs()))

