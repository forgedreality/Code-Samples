locations = {
    'North America' : {'USA' : ['Mountain View', 'Atlanta']},
    'Asia' : {
        'India' : ['Bangalore'],
        'China' : ['Shanghai']
    },
    'Africa' : { 'Egypt' : ['Cairo']}
}

print('1')
print('\n'.join(sorted(i for i in locations['North America']['USA'])))
print('2')

# sort by city name
itr = sorted(locations['Asia'].items(), key = lambda kv:(kv[1], kv[0]))
for i in itr:
    for j in i[1]:
        print(j, '-', i[0])

''' ----------------- '''

"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000
    
    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        valA = ord(string[0])
        valB = ord(string[1])
        res = (valA * 100) + valB
        return res

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        hash_value = self.calculate_hash_value(string)
        if hash_value != -1:
            if self.table[hash_value] != None:
                self.table[hash_value].append(string)
            else:
                self.table[hash_value] = [string]

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        hash_value = self.calculate_hash_value(string)
        if hash_value != -1:
            if self.table[hash_value] != None:
                if string in self.table[hash_value]:
                    return hash_value
        return -1    
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print(hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print(hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print(hash_table.lookup('UDACIOUS'))

