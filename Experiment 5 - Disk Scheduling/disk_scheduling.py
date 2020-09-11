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
    head_movement= []
    head_movement.append(head)
    for req in request_queue:
        movement += abs(req - prev_head)
        # print(req, " - ", prev_head, "= ", abs(req - prev_head), " | total movement = ", movement)
        head_movement.append(req)
        prev_head = req
    head_movement_path(head_movement)
    print("Total Head Movement = ", movement)

def scan(request_queue, head):
    prev_head = head
    movement = 0
    head_movement = []
    head_movement.append(head)
    for req in range(head, 200):
        if req in request_queue:
            movement += abs(req - prev_head)
            prev_head = req
            head_movement.append(req)
            request_queue.remove(req)
    for req in range(200, 0, -1):
        if req in request_queue:
            movement += abs(req - prev_head)
            prev_head = req
            head_movement.append(req)
            request_queue.remove(req)

    head_movement_path(head_movement)
    print("Total Head Movement : ", movement)



def main():
    print("Enter the no. of request : ")
    n = int(input())
    print("Enter Head Position : ")
    head = int(input())
    print("Provide the positions to visit (max:200) : ")
    request_queue = []
    for i in range(n):
        req_pos = int(input())
        request_queue.append(req_pos)
    # head = request_queue[0]
    fcfs(request_queue, head)
    scan(request_queue, head)
    



def test():
    pass



if(len(sys.argv) > 1 and sys.argv[1] == 'test'):
    test()
else:
    main()
