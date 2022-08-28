"""DINI IRDINA AHMAD UBAIDAH
   31279279"""

def find_max(myList):
    maximum = myList[0]
    for item in myList:
        if item > maximum:
            maximum = item
    return maximum

def radix_sort(myList):
    """Function sorts the given list of integers by starting from the rightmost digit of each number until it reaches
       the leftmost digit. It utilises method of counting sort to do this repeatedly for each digit while preserving the
       ordering of the prior sort, until all digits have been considered.

       Example Input: radix_sort([11, 1, 3, 1, 4, 10, 5, 7, 10])
       Example Output: [1, 1, 3, 4, 5, 7, 10, 10, 11]

       Time Complexity: Worst-case complexity of O(KN) where K is the number of columns/digits and N is the number of items in the list.
                        Best-case complexity is the same O(KN).
       Auxiliary Space: O(N) where N is the number of items in the list."""
    if myList == []:
        return []

    base = 10
    max_item = find_max(myList)
    count_array = [[None]]*(10)

    for i in range(len(count_array)):
        count_array[i] = []

    count_digits = 0
    while max_item != 0:
        max_item = max_item//10
        count_digits += 1
    
    for x in range(count_digits):
        for y in range(len(count_array)): #initalizing count_array to empty values again
            count_array[y] = []

        for i in range(len(myList)):
            num = (myList[i]//(base**x))%base
            count_array[num].append(myList[i])
        
        index = 0
        for number in range(len(count_array)):
            frequency = len(count_array[number])
            for freq in range(frequency):
                myList[index] = count_array[number][freq]
                index += 1
    return myList


def best_interval(transactions, t):
    """This function accepts an unsorted list of non-negative integers, transactions, and a non-negative integer
       that represents a length of time, t. The function returns a tuple (best_t, count) where best_t is the time
       such that the interval starting at best_t and ending at best_t+t contains the most elements from transactions.
       Count is the number of elements in the interval.

       It starts by sorting the list using radix sort, then with the sorted list we use pointers to keep count of the 
       intervals and their elements. Every interval is appended to a an array, interval_array, and once we have gone through
       the entire transactions list, we loop through the interval_array to find the tuple with the biggest count. This tuple
       is the desired output.

       Example Input: best_interval([11, 1, 3, 1, 4, 10, 5, 7, 10], 5)
       Example Output: (0, 5)

       Time Complexity: Worst-case complexity of O(NK) where N is the number of elements in transactions and K is the greatest
                        number of digits in any element in transactions.
                        Best-case complexity is the same as worst-case O(NK).
       Auxiliary Space: O(N+M) where N is the number of items in the list and M is the number of intervals found (interval_array).
       """
    if transactions == []:
        return (0,0)
    transactions = radix_sort(transactions)
    interval_array = []

    pointer1 = 0
    pointer2 = 0
    count = 0
    max_num = transactions[0] + t

    while pointer2 < len(transactions):
        if transactions[pointer2] > max_num:
            good_t = transactions[pointer2-1] - t
            if good_t >= 0:
                interval_array.append((good_t, count))
            else:
                interval_array.append((0,count))
            count -= 1
            pointer1 += 1
            max_num = transactions[pointer1] + t
        elif pointer2 == len(transactions)-1:
            good_t = transactions[pointer2] - t
            count += 1
            if good_t >= 0:
                interval_array.append((good_t, count))
            else:
                interval_array.append((0,count))
            break
        else:
            count += 1
            pointer2 += 1

    max_interval = interval_array[0]
    for i in range(len(interval_array)):
        if interval_array[i][1] > max_interval[1]:
            max_interval = interval_array[i]
    return max_interval


def find_max_length(myList):
    """Finds the length (number of characters) of the longest String."""
    max_length = 0
    for i in range(len(myList)):
        if len(myList[i]) > max_length:
            max_length = len(myList[i])
    return max_length


def radix_sort_strings(myList):
    """This function is used to sort a list of Strings in lexicographical order. It accepts a list of Strings as input
       and returns the sorted version of the list.

       Example Input: radix_sort_strings(["spot", "tops", "dad", "simple", "dine", "cats"])
       Example output: ["cats", "dad", "dine", "simple", "spot", "tops"]

       Time Complexity: Worst-case complexity of O(NK) where N is the number of items in the list and K is the number of
                        characters of the longest string in the list.
                        Best-case complexity is the same as worst-case O(NK).
       Auxiliary Space: O(N) where N is the number of items in the list.
       """
    max_length = find_max_length(myList)
    count_array = [[None]] *27

    for i in range(len(count_array)):
        count_array[i] = []

    for x in range(max_length, 0, -1):
        for y in range(len(count_array)):
            count_array[y] = []

        for i in range(len(myList)):
            if len(myList[i]) < x:
                count_array[0].append(myList[i])
            else:
                num = ord(myList[i][x-1]) - 96
                count_array[num].append(myList[i])

        index = 0
        for word in range(len(count_array)):
            for position in range(len(count_array[word])):
                myList[index] = count_array[word][position]
                index += 1
    return myList

def radix_sort_strings_index(myList):
    """This function is used in words_with_anagrams() to sort the list that has both Strings and their indexes.
       It is identical to the function radix_sort_strings() with the exception that it sorts the Strings but maintains/keeps
       their original position index.

       Example Input: radix_sort_strings_index([["spot", 0], ["tops", 1], ["dad", 2], ["simple", 3], ["dine", 4], ["cats", 5]])
       Example output: [["cats", 5], ["dad", 2], ["dine". 4], ["simple", 3], ["spot", 0], ["tops", 1]]

       Time Complexity: Worst-case complexity of O(NK) where N is the number of items in the list and K is the number of
                        characters of the longest string in the list.
                        Best-case complexity is the same as worst-case O(NK).
       Auxiliary Space: O(N) where N is the number of items in the list."""
    max_length = 0
    for i in range(len(myList)):
        if len(myList[i][0]) > max_length:
            max_length = len(myList[i][0])

    count_array = [[None]] *27

    for i in range(len(count_array)):
        count_array[i] = []

    for x in range(max_length, 0, -1):
        for y in range(len(count_array)):
            count_array[y] = []

        for i in range(len(myList)):
            if len(myList[i][0]) < x:
                count_array[0].append(myList[i])
            else:
                num = ord(myList[i][0][x-1]) - 96
                count_array[num].append(myList[i])

        index = 0
        for word in range(len(count_array)):
            for position in range(len(count_array[word])):
                myList[index] = count_array[word][position]
                index += 1
    return myList

def alphabetical_sort(word):
    """This function sorts the characters of a String/word in alphabetical order. Utilises counting sort method.
    
       Example Input: alphabetical_sort("cats")
       Example Output: "acst"

       Time Complexity: Worst-case of O(N) where N is the length of the input String
                        Best-case is the same as worst-case O(N)
       Auxiliary Space: O(M) where M is the number of characters (26 in this case)"""
    countArray = [0] * 26
    for item in word:
        wordChar = ord(item) - 97
        countArray[wordChar] += 1

    newArray = []
    newString = ""
    for i in range(len(countArray)):
        frequency = countArray[i]
        for _ in range(frequency):
            newArray.append(chr(i+97))
    return newString.join(newArray)


def words_with_anagrams(list1, list2):
    """This function takes in two lists of Strings as input and outputs a list of Strings from list1 which have 
       at least one anagram appearing in list2. First, it sorts both the input lists in lexicographical order using
       radix sort. Then it creates 2 new lists that contains the alphabetically sorted versions of the Strings as well
       as their position indexes from the sorted input lists. The indexes are used to retrieve the original form of the string.
       It then utilises pointers in each list to check if an anagram exists and if it does, it will append the String from
       the input list into the array, anagram_list.
       
       Example Input: list1 = [spot, tops, dad, simple, dine, cats]
                      list2 = [pots, add, simple, dined, acts, cast]
                      words_with_anagrams(list1, list2)
       Example Output: [cats, dad, simple, spot, tops]

       Time Complexity: Worst-case complexity of O(L1M1+L2M2) where L1 is the number of elements in list1, L2 is the number
                        of elements in list2, M1 is the number of characters in the longest string in list1, and M2 is the
                        number of characters in the longest string in list2.
                        Best-case complexity is the same as worst-case O(L1M1+L2M2).
       Auxiliary Space: O(L1+L2+L3) where L1 is the number of elements in list1 and L2 is the number of elements in list2,
                        and L3 is the size of anagram_list.
       """
    list1 = radix_sort_strings(list1)
    list2 = radix_sort_strings(list2)
    scrambledList1 = []
    scrambledList2 = []
    for i in range(len(list1)):
        scrambledList1.append([alphabetical_sort(list1[i]),i])
    for i in range(len(list2)):
        scrambledList2.append([alphabetical_sort(list2[i]),i])
    scrambledList1 = radix_sort_strings_index(scrambledList1)
    scrambledList2 = radix_sort_strings_index(scrambledList2)
    anagram_list = []
    pointer1 = 0
    pointer2 = 0

    while pointer1 < len(list1) and pointer2 < len(list2):
        if scrambledList1[pointer1][0]== scrambledList2[pointer2][0]:
            position = scrambledList1[pointer1][1]
            anagram_list.append(list1[position])
            pointer1 += 1
        elif scrambledList1[pointer1][0]> scrambledList2[pointer2][0]:
            pointer2 += 1
        elif scrambledList1[pointer1][0] < scrambledList2[pointer2][0]:
            pointer1 += 1

    return anagram_list



# take a break T_T