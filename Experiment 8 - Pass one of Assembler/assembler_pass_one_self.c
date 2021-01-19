#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void main(){
    FILE *inp, *optab, *symtab;
    int locctr, starting_addr, l, operand, o, len, addr_optable;
    char label[20], opcode[20], op[20], opcode_optable[20];

    // Opening files
    inp = fopen("input.txt", "r");
    symtab = fopen("symtab_self.txt","w");

    // Initializing locctr
    fscanf(inp, "%s %s %d", label, opcode, &operand);
    if(strcmp(opcode, "START") == 0){
        starting_addr = operand;
        locctr = starting_addr;
        printf("\t%s\t%s\t%d\n", label, opcode, operand);
    }else{
        locctr = 0;
    }

    // Reading first label and opcode
    fscanf(inp, "%s %s", label, opcode);

    // loop until end of input file
    while(!feof(inp)){
        // Scanning the operand of the line whose label and opcode are scanned above
        fscanf(inp, "%s", op);
        printf("\n%d\t%s\t%s\t%s\n", locctr, label, opcode, op);

        // Checking if label is present
        if(strcmp(label, "-") != 0){
            fprintf(symtab, "\n%d\t%s\t%s\t%s\n", locctr, label, opcode, op);
        }

        // Getting addr of opcode from optable
        optab = fopen("optab.txt", "r");
        fscanf(optab, "%s %d", opcode_optable, &addr_optable);
        while(!feof(optab)){
            if(strcmp(opcode, opcode_optable) == 0){
                locctr += 3;
                break;
            }
            fscanf(optab, "%s %d", opcode_optable, &addr_optable);
        }
        fclose(optab);

        // Incrementing locctr based on the opcode
        if(strcmp(opcode, "WORD") == 0){
            locctr +=3;
        }else if(strcmp(opcode, "RESW") == 0){
            operand = atoi(op);
            locctr += 3*operand;
        }else if(strcmp(opcode, "BYTE") == 0){
            if(op[0] == 'X'){
                locctr += 1;
            }else{
                len = strlen(op) - 3;
                locctr += len;
            }
        }else if(strcmp(opcode, "RESB") == 0){
            operand = atoi(op);
            locctr += operand;
        }

        fscanf(inp, "%s %s", label, opcode);
    }
    if(strcmp(opcode,"END")==0){
        printf("\nProgram Length = %d",locctr-starting_addr);
    }
    fclose(inp);
    fclose(symtab);
    printf("\n");
}