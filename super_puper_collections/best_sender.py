from collections import defaultdict


def best_sender(messages, senders):
    result = defaultdict(int)
    for messag, sender in zip(messages, senders):
        result[sender] += len(messag.split())

    return max(result.items(), key=lambda x: (x[1], x[0]))[0]


messages = ["Hi, Linda", "Hi, Sam", "How are you doing?"]
senders = ["Sam Fisher", "Linda", "Sam Fisher"]
print(best_sender(messages, senders))
