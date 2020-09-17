import sys
from termcolor import colored


def print_req(request_queue):
    for req in request_queue:
        print(req, end="  ")
    print()

def head_movement_path(head_movement):
    print()
    for item in head_movement:
        print(colored(item, "blue"), end=colored(" -> ", "green"))
    print(colored("END", "red"))
    print()


def fcfs(request_queue, head):
    movement = 0
    prev_head = head
    head_movement= []
    head_movement.append(head)
    for req in request_queue:
        movement += abs(req - prev_head)
        head_movement.append(req)
        prev_head = req
    print(colored("\n----------FCFS Scheduling----------","yellow"))
    head_movement_path(head_movement)
    print("Total Head Movement = ", colored(movement,"blue"))
    print(colored("-----------------------------------\n","yellow"))

def scan(req_queue, head):
    request_queue = req_queue[:]
    prev_head = head
    movement = 0
    head_movement = []
    head_movement.append(head)
    # print("Movement : ")
    for req in range(head, 200):
        if req in request_queue:
            movement += abs(req - prev_head)
            # print("From", prev_head, "to ", req, " Movement = ", abs(req- prev_head), "  Total movement till now : ", movement)
            prev_head = req
            head_movement.append(req)
            request_queue.remove(req)
    movement += abs(prev_head - 200)
    # print("Movement to 200 : ",abs(prev_head - 200), " Total Movement : ", movement )
    prev_head = 198
    for req in range(200, 0, -1):
        if req in request_queue:
            movement += abs(req - prev_head)
            # print("From", prev_head, "to ", req, " Movement = ", abs(req- prev_head), "  Total movement till now : ", movement)
            prev_head = req
            head_movement.append(req)
            request_queue.remove(req)

    print(colored("\n----------SCAN Scheduling----------","yellow"))
    head_movement_path(head_movement)
    print("Total Head Movement : ", colored(movement,"blue"))
    print(colored("-----------------------------------\n","yellow"))

def cscan(req_queue, head):
    request_queue = req_queue[:]
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
    movement += abs(prev_head - 200)
    # 198 since we're going to 0 and 200
    movement += 198
    prev_head = 0
    for req in range(0, 200):
        if req in request_queue:
            movement += abs(req - prev_head)
            prev_head = req
            head_movement.append(req)
            request_queue.remove(req)

    print(colored("\n----------CSCAN Scheduling----------","yellow"))
    head_movement_path(head_movement)
    print("Total Head Movement : ", colored(movement,"blue"))
    print(colored("-----------------------------------\n","yellow"))



def main():
    print("Enter the no. of request : ")
    n = int(input())

    print("Enter Head Position : ")
    head = int(input())

    print("Provide the positions to visit (max:200) : ")
    request_queue = [int(x) for x in input().split()]

    fcfs(request_queue, head)
    scan(request_queue, head)
    cscan(request_queue, head)
    



def test():
    pass



if(len(sys.argv) > 1 and sys.argv[1] == 'test'):
    test()
else:
    main()
