VOWELS = 'aeiou'
def transform_file(file_name):
    with open(file_name,'r') as obj:
        res = ''
        for line in obj.readlines():
            line_res = ' '.join([
                word + 'way' if word[0] in VOWELS else word[1:] + word[0] + 'ay'
                for word in line.split(' ')
            ])
            res = f'{res}{line_res}\n'

    return res


if __name__ == '__main__':
    transform_file('sample.txt')

