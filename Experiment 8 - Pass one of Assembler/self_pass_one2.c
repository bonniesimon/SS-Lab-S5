#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void main(){
    FILE *inp, *symtab, *optab;
    int start_addr, locctr;
    int optab_mne, optab_addr, operand;
    char label[20], mne[20], opnd[20], addr[20];
    inp = fopen("input.txt", "r");
    symtab = fopen("symtab_self.txt","w");
    optab = fopen("optab.txt", "r");

    fscanf(inp, "%s%s%s", label, mne, opnd);
    if(strcmp(mne, "START") == 0){
        start_addr = atoi(opnd);
        locctr = start_addr;
        printf("\t%s\t%s\t%s\n", label, mne, opnd);
    }else{
        locctr = 0;
    }

        fscanf(inp, "%s%s", label, mne);

    while(!feof(inp)){
        fscanf(inp, "%s", opnd);
        printf("%d\t%s\t%s\t%s\n", locctr, label, mne, opnd);

        if(strcmp(label, "-") != 0){
            fprintf(symtab, "\n%d\t%s\t%s\t%s\n", locctr, label, mne, opnd);
        }

        fscanf(optab, "%s%s", optab_mne, optab_addr);
        while(!feof(optab)){
            if(strcmp(mne, optab_mne) == 0){
                locctr += 3;
                break;
            }
            fscanf(optab, "%s%s", optab_mne, optab_addr);
        }
        fclose(optab);

        if(strcmp(mne, "WORD") == 0){
            locctr += 3;
        }else if(strcmp(mne, "RESW") == 0){
            operand = atoi(opnd);
            locctr += 3*operand;
        }else if(strcmp(mne, "BYTE") == 0){
            if(opnd[0] = "X"){
                locctr +=1;
            }else{
                locctr += strlen(opnd) - 3;
            }
        }else if(strcmp(mne, "RESB") == 0){
            operand = atoi(opnd);
            locctr += operand;
        }
        fscanf(inp, "%s%s", label, mne);
    }
    if(strcmp)
}