
def prevedi_slovo_u_broj(slovo):
    if 'a' <= slovo <= 'h':
        broj = ord(slovo) - ord('a')
        return broj
    else:
        print("Uneto slovo nije u rasponu od 'a' do 'h'.")
        return -1