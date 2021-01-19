#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

void main(){
    FILE *inp, *optab, *symtab, *flen;
    int len;
    char label[20], addr[20], mne[20], operand[20], start_addr[20], opmne[20], opcode[20], symaddr[20], symmne[20];

    // opening files
    inp = fopen("input.txt", "r");
    optab = fopen("optab.txt", "r");
    symtab = fopen("symbol.txt", "r");
    flen = fopen("length.txt", "r"); 

    // reading line
    fscanf(inp, "%s %s %s %s", addr, label, mne, operand);

    // Taking starting address into start_addr & len from file
    if(strcmp(mne, "START") == 0){
        strcpy(start_addr, operand);
        fscanf(flen, "%d", &len);
    }

    //Printing first Header record
    printf("H^%s^%s^%d\n", label, start_addr, len);
    // Printing beginning of next Text Record
    printf("T^00%s^", start_addr);

    // Reading next input line
    fscanf(inp, "%s %s %s %s", addr, label, mne, operand);

    // check if END mnemonic
    while(strcmp(mne, "END") != 0){

        // reading from optab
        fscanf(optab, "%s %s", opmne, opcode);
        // checking if omne is a valid opcode
        while(!feof(optab)){
            if(strcmp(mne, opmne) == 0){
                fclose(optab);
                // reading from symtab
                fscanf(symtab, "%s %s", symaddr, symmne);
                // checking if operand is a valid one
                while(!feof(optab)){
                    if(strcmp(operand, symmne) == 0){
                        printf("%s%s^", opcode, symaddr);
                        break;
                    }
                    fscanf(symtab, "%s %s", symaddr, symmne);
                }
                break;
            }
            fscanf(optab, "%s %s", opmne, opcode);
        }
        if(strcmp(mne, "BYTE") == 0 || strcmp(mne, "WORD") == 0){
            if(strcmp(mne, "WORD") == 0){
                printf("0000%s^", operand);
            }else{
                len = strlen(operand);
                for(int i = 2; i<len; i++){
                    printf("%d", operand[i]);
                }
                printf("^");
            }
        }
        fscanf(inp, "%s %s %s %s", addr, label, mne, operand);
        optab = fopen("optab.txt", "r");
        fseek(optab, SEEK_SET, 0);
    }
    printf("\nE^00%s", start_addr);
    fclose(inp);
    fclose(optab);
    fclose(symtab);
    fclose(flen);
}