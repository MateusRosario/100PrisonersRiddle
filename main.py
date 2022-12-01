from random import shuffle, randint


def random_search(prisoners_num):
    boxes = [label for label in range(prisoners_num)]
    shuffle(boxes)

    success = True
    for prisoner in range(prisoners_num):
        opened_boxes = []
        found = False
        for tentativa in range(int(prisoners_num/2)):
            box = randint(0, prisoners_num - 1)
            # se caixa já está aberta, escolhe outra para abrir
            while box in opened_boxes:
                box = randint(0, prisoners_num - 1)

            paper = boxes[box]
            opened_boxes.append(box)
            if paper is prisoner:
                found = True
                break
        if not found:
            success = False
            break

    return success


def loop_search(prisoners_num):
    boxes = [i for i in range(prisoners_num)]
    shuffle(boxes)

    success = True
    for prisoner in range(prisoners_num):
        last_paper = prisoner
        found = False
        for tentativa in range(int(prisoners_num/2)):
            paper = boxes[last_paper]
            last_paper = paper
            if paper is prisoner:
                found = True
                break
        if not found:
            success = False
            break

    return success


def evaluate_searches(num, function):
    sucesses = 0
    for ev in range(num):
        # print(function.__name__, ':', ev)
        sucesses += 1 if function(prisoners_number) else 0

    return sucesses/num


if __name__ == '__main__':
    prisoners_number = 100
    range_evaluation = 100000

    print(f'Success rate on random search: {evaluate_searches(range_evaluation, random_search)}')
    print(f'Success rate on loop search: {evaluate_searches(range_evaluation, loop_search)}')
