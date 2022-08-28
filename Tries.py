#DINI IRDINA AHMAD UBAIDAH, 31279279

class Node:
    def __init__(self, num):
        self.link = [None] * 5
        self.freq = 0
        self.mostfreq = 0
        self.freq_word = ""
        self.index = num

class SequenceDatabase:
    def __init__(self):
        """Initialising the root of the Trie."""
        self.root = Node(0)

    def addSequence(self, s):
        """This function stores s into the database represented by the instance of SequenceDatabase. It
           uses self.insert_recur_aux() to recursively store each character of s into the Trie.

           Time Complexity: Worst Case of O(len(s)) where s is the input String.
                            Best Case is the same as worst case, O(len(s)).

           Space Complexity: O(len(s)) wheres is the input String."""
        current = self.root
        self.insert_recur_aux(current, s,0)

    def insert_recur_aux(self,current, text, num=0):
        """This recursive function creates and inserts new nodes into the Trie, and if the node already exists, it
           updates its frequency. When it reaches the end of the given text, if the text is an existing word it will
           simply increase the node's frequency, if not it will insert a new node and update its frequency.
           Then it will proceed to return this frequency (this will stay unchanged throughout all the recursive returns).
           This value is then passed all the way back to the root and at each node it passes, it will check if the
           frequency passed is greater than the current highest frequency. If it is, replace the most frequent word and
           replace its frequency. If it is the same frequency, check if the index of the node is smaller than the
           character at the same position of the current highest word. If it is, replace the most frequent word.

           Time Complexity: Worst Case of O(len(s)) where s is the input String.
                            Best Case is the same as worst case, O(len(s)).

           Space Complexity: O(len(s)) wheres is the input String."""

        if num == len(text) :  #checks if end of string
            if current.link[0] is None:  #checks if new word
                current.link[0] = Node(0)
                new_current = current.link[0]
                new_current.freq += 1
                new_current.mostfreq += 1
                new_current.freq_word = text
            else:
                new_current =current.link[0]
                new_current.freq += 1
                new_current.mostfreq += 1
            if new_current.mostfreq > current.mostfreq:  #checks if higher frequency
                current.mostfreq = new_current.mostfreq
                current.freq_word = text
                return current.mostfreq
            elif new_current.mostfreq == current.mostfreq:  #if same frequency, check if lexicographically smaller
                if num < len(current.freq_word) and new_current.index < ord(current.freq_word[num])-65+1:
                    current.freq_word = text
                    return current.mostfreq
            return new_current.mostfreq
        else:
            index = ord(text[num]) - 65 + 1
            if current.link[index] is not None:
                current = current.link[index]
                current.freq += 1
            else:
                current.link[index] = Node(index)
                current = current.link[index]
                current.freq += 1
            result = self.insert_recur_aux(current, text, num+1)  #recursive call
            if result > current.mostfreq:  #if new word has higher frequency than the current most frequent word
                current.mostfreq = result
                current.freq_word = text
            elif result == current.mostfreq:
                if num <= len(current.freq_word) and current.index < ord(current.freq_word[num-1]) - 65 + 1:
                    current.freq_word = text
            return result

    def query(self, q):
        """This function accepts a String, q, as a prefix. This prefix is then used to determine and return the most
           frequent word that has q as a prefix. If two or more strings are tied for most frequent, it returns the
           lexicographically least of them. If there are no strings that have q as a prefix, it returns None. If the
           prefix given is an empty string, the function will return the most frequent word at the first node it finds.

           Example Input: db.addSequence("ABCD")
                          db.addSequence("ABC")
                          db.addSequence("ABC")
                          db.query("A")

           Example Output: "ABC"


           Time Complexity: O(len(q)) where q is the prefix string entered.

           Space Complexity: O(1) as we are only querying from existing items in the database and no items are created."""

        current = self.root
        if len(q) == 0:
            if current.link[1] is not None:
                return current.link[1].freq_word
            elif current.link[2] is not None:
                return current.link[2].freq_word
            elif current.link[3] is not None:
                return current.link[3].freq_word
            elif current.link[4] is not None:
                return current.link[4].freq_word

        for char in q:
            index = ord(char) - 65 +1
            if current.link[index] is not None:
                current = current.link[index]
            else:
                return None

        return current.freq_word


class OrfNode:
    def __init__(self):
        self.link = [None]* 5
        self.data = []

class OrfFinder:
    def __init__(self, genome):
        """This function initialises the suffix trie and prefix trie of genome. For the suffix trie, it loops through
           the nodes and appends the start indexes of the suffixes. For the prefix trie, it works the same way except it
           starts from the back of the string and stores the end indexes of the prefixes.

           Time Complexity: Worst Case of O(N^2) where N is the length of genome (input String).
                            Best Case is the same as worst case, O(N^2).

           Space Complexity: O(N^2) where N is the length of genome(input String)."""
        self.rootSuffix = OrfNode()
        self.rootPrefix = OrfNode()
        self.text = genome

        for i in range(len(genome)):
            currentSuffix = self.rootSuffix
            for j in range(i, len(genome)):
                index= ord(genome[j])-65+1
                if currentSuffix.link[index] is not None:
                    currentSuffix = currentSuffix.link[index]
                    currentSuffix.data.append(i)
                else:
                    currentSuffix.link[index] = OrfNode()
                    currentSuffix = currentSuffix.link[index]
                    currentSuffix.data.append(i)

        for i in range(len(genome)-1,-1,-1):
            currentPrefix = self.rootPrefix
            for j in range(i,-1,-1):
                index = ord(genome[j]) - 65 + 1
                if currentPrefix.link[index] is not None:
                    currentPrefix = currentPrefix.link[index]
                    currentPrefix.data.append(i)
                else:
                    currentPrefix.link[index] = OrfNode()
                    currentPrefix = currentPrefix.link[index]
                    currentPrefix.data.append(i)


    def find(self,start,end):
        """This function accepts as input a string, start, and another string, end. The function returns a list of
           substrings that have start as a prefix and end as a suffix. It loops through the suffix trie N number of times
           where N is the length of start. Once it reaches the end, it takes in the data at that node as the list of suffix indexes.
           This process is repeated for the prefix trie where it loops N number of times and N is the length of end.
           Once it has the list of indexes for both prefix and suffix, it generates all the possible strings and appends
           the ones that meet the conditions.

           Example Input: genome1 = OrfFinder("AAABBBCCC")
                  genome1.find("AAA","BB")

           Example Output: ["AAABB","AAABBB"]

           Time Complexity: O(len(start)+len(end)+U) where U is the number of characters in the output list.

           Space Complexity: O(N+M+Z) where N is the result list generated, M is the suffixIndex list created, Z is the
                             prefixIndex list created."""
        currentSuffix = self.rootSuffix
        currentPrefix = self.rootPrefix
        string_length = len(start)+len(end)
        suffixIndexes = []
        prefixIndexes = []
        result = []

        for i in range(len(start)):  #loop for getting list of suffix indexes
            index = ord(start[i])-65+1
            if currentSuffix.link[index] is not None:
                currentSuffix = currentSuffix.link[index]
                if i == len(start)-1:
                    suffixIndexes = currentSuffix.data
            else:
                suffixIndexes = None
                break

        endlength = len(end)
        for i in range(len(end)):  #loop for getting list of prefix indexes
            index = ord(end[endlength-1-i])-65+1
            if currentPrefix.link[index] is not None:
                currentPrefix = currentPrefix.link[index]
                if i == endlength-1:
                    prefixIndexes = currentPrefix.data
            else:
                prefixIndexes = None
                break

        if prefixIndexes is None or suffixIndexes is None:
            return []
        else:
            for i in range(len(suffixIndexes)):
                for j in range(len(prefixIndexes)):
                    if suffixIndexes[i] <= prefixIndexes[j]:  #ensures the string slicing process will be carried out properly
                        word = self.text[suffixIndexes[i]:prefixIndexes[j]+1]
                        if len(word)>=string_length:
                            result.append(word)
        return result

