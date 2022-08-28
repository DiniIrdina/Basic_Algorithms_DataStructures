def best_schedule(weekly_income, competitions):
    """This function accepts as input a list of non-negative integers, weekly_income, that represents the weekly income
       from working as a trainer, and a list of tuples, competitions, where each tuple represents a competition's
       preparation start and end week, and the money attainable from it. It then combines these two inputs and sorts it
       according to the end week. Once sorted, through memoization it then decides which possible combination of weekly
       income and competitions would produce the optimum amount of money, and returns this maximum income.

       Example Input: weekly_income = [3,7,2,1,8,4,5]
                      competitions = [(1,3,15),(2,2,8),(0,4,30),(3,5,19)]
                      best_schedule(weekly_income, competitions)
       Example Output: 42

       Time Complexity: Worst-case complexity of O(N log(N)) where N is the total number of elements in weekly_income
                        and competitions combined.
                        Best-case complexity is the same as worst-case O(N log(N)).
       Space Complexity: O(N) where N is the total number of elements in weekly_income and competitions combined.
    """
    if not weekly_income and not competitions:
        return 0
    elif not weekly_income:
        return 0

    training_income = []
    for i in range(len(weekly_income)):
        training_income.append([i,i, weekly_income[i]])

    memo = [0] * (len(training_income)+1)
    comp_train = training_income + competitions
    comp_train.sort(key = lambda x: x[1])

    for j in range(len(comp_train)):
        start = comp_train[j][0] + 1
        end = comp_train[j][1] + 1
        income = comp_train[j][2]
        if memo[end] < memo[start-1] + income:
            memo[end] = memo[start-1] + income
    return memo[-1]

def best_itinerary(profit, quarantine_time, home):
    """This function accepts three inputs, a list of lists called profits, where profit[d][c] represents the profit
        attainable by working in city c on day d, as well as a list of non-negative integers, quarantine_time, where each
        item represents the number of quarantine days required by each city. The final input is home, an integer that
        represents the city that we start in. The function decides whether to stay, travel, or quarantine in order to
        obtain the optimum profit. To do this, it checks the previous items in the memo to gauge if it more profitable
        to add to the existing pattern(previous day, same city), or if it is better to have traveled from the previous city
        and to start working at the current city today. In this implementation, we select the maximum profit from the last
        position (final day) in the memo and returns this result.

        Example Input: profit = [[6, 9, 7, 5, 9],[4, 7, 3, 10, 9],[7, 5, 4, 2, 8],[2, 7, 10, 9, 5],[2, 5, 2, 6, 1],
                                 [4, 9, 4, 10, 6],[2, 2, 4, 8, 7],[4, 10, 2, 7, 4]]
                       quarantine_time = [3,1,1,1,1]
                       best_itinerary(profit, quarantine_time, 0)
        Example Output: 39

        Time Complexity: Worst-case complexity of O(nd) where n is the number of cities, and d is the number of days.
                         Best-case complexity is the same as worst-case O(nd).
        Space Complexity: O(nd) where n is the number of cities and d is the number of cities."""

    memo = [[None]] * (len(profit)+1)

    for i in range(len(memo)):
        memo[i] = [0] * len(quarantine_time)

    for i in range(1,len(memo)):
        memo[i][home] = memo[i-1][home]+profit[i-1][home]

    for day in range(1, len(profit) + 1):
        for city in range(len(quarantine_time)):
            moveDays = abs(city-home)
            if city != home:
                moveDays += quarantine_time[city]
            if moveDays >= day:
                continue
            differenceDay = day - moveDays
            if city >= home:
                startHere = memo[differenceDay - 1][city - 1] + profit[day - 1][city]
            else:
                startHere = memo[differenceDay - 1][city + 1] + profit[day - 1][city]
            previousStart = memo[day-1][city] + profit[day-1][city]
            if startHere > previousStart:
                memo[day][city] = startHere
            else:
                memo[day][city] = previousStart
    return (max(memo[-1]))
