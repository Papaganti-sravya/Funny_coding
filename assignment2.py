
NAME:Sravya Papaganti 

import json
import statistics
unique_name = []
unique_language = []
for readLine in open("C://Users/nagar/Downloads/Spark - Copy.json"):
    dataRow = json.loads(readLine)

#question1#
    for element in dataRow:
        print(element)
        for key,value in element.items():
            if key == 'username':
                unique_name.append(value)
            if key == 'language':
                unique_language.append(value)
    
    print("Question 1")
    print("unique name : ",len(set(unique_name)))
    print("unique language: ",len(set(unique_language)))

    #question 2 avg and median of stars for each language
    count_language = {}
    for element in dataRow:
        for key, value in element.items():
            if key == 'language':
                key_value = value
                print("key: ",key_value)
            if key == 'stars':
                value_value = value
        #print("key: ",key_value)
        #print("Value: ", value_value)
        if key_value  not in count_language:
            count_language[key_value] = [value_value]
        else:
            count_language[key_value].append(value_value)
    print(count_language)
    print(len(count_language))

    for key, value in  count_language.items():
        print("Keys : ", key)
        print("values : ", value)
        print("Average : ", key ,": ", (sum(value) / len(value)))
        print("Median : ",key ,": ",statistics.median(value) )

    
    #question 3:
    open_issues = {}
    for element in dataRow:
        for key, value in element.items():
            if key == 'language':
                key_value = value
                print("key: ",key_value)
            if key == 'open_issues':
                value_value = value
        # print("key: ",key_value)
        # print("Value: ", value_value)
        if key_value not in open_issues:
            open_issues[key_value] = [value_value]
        else:
            open_issues[key_value].append(value_value)

        #print(open_issues)
        for key, value in open_issues.items():
            #print("Keys : ", key)
            #print("values : ", value)
            print("Min : ", min(value))
            print("Max : ", max(value))
            print("AVG : ", sum(value)/len(value))
            print("Medium : ", statistics.median(value))

    
    #question 4
    fork = []
    subscriber = []
    for element in dataRow:
        for key, value in element.items():
            if key == 'forks':
                fork.append(value)
            if key == 'subscribers':
                subscriber.append(value)
    fork_value = int(input("Please give fork value: "))
    subscriber_value = int(input("Please give subscriber value: "))
    fork_result = []
    subscriber_result = []
    for i in fork:
        if fork_value <= i:
            fork_result.append(i)

    for j in subscriber:
        if subscriber_value <= j:
            subscriber_result.append(j)
            #print("subscriber value: ", j)
    print("fork value: ",fork_result)
    print("subscriber value: ",subscriber_result)


    #question 5
    topic_value = input(str("Enter string value : "))
    count = 0
    for element in dataRow:
        for key, value in element.items():
            if key == 'topics':
                print(value)
                for values in value:
                    if values == topic_value:
                        print("value: ", values, " row: ", value)
                        count = count+1
    print("Topic : ", topic_value, "Count : ", count)



