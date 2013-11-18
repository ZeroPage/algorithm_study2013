#Skywave

inputData = raw_input().split()
notes = [-1]

for i in range(int(inputData[0])):
    notes.append(notes[i] + int(raw_input()))

notesLength = len(notes)

for i in range(int(inputData[1])):
    target = int(raw_input())
    head = 0
    tail = notesLength - 1

    while tail != head + 1:
        half = (head + tail) / 2
        if target > notes[half]:
            head = half
        else:
            tail = half

    print tail
