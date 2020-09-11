import sys


def print_req(request_queue):
    for req in request_queue:
        print(req, end="  ")
    print()

def head_movement_path(head_movement):
    for item in head_movement:
        print(item, end="-> ")
    print("END")


def fcfs(request_queue, head):
    movement = 0
    prev_head = head
    for req in request_queue:
        movement += abs(req - prev_head)
        # print(req, " - ", prev_head, "= ", abs(req - prev_head), " | total movement = ", movement)
        prev_head = req
    head_movement_path(request_queue)
    print("Total Head Movement = ", movement)


def main():
    print("Enter the no. of request : ")
    n = int(input())
    print("Provide the positions to visit (max:200) : ")
    request_queue = []
    for i in range(n):
        req_pos = int(input())
        request_queue.append(req_pos)
    head = request_queue[0]
    fcfs(request_queue, head)
    



def test():
    pass



if(len(sys.argv) > 1 and sys.argv[1] == 'test'):
    test()
else:
    main()
