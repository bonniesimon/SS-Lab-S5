#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

void main(){
    FILE *inp, *optab, *symtab, *flen;
    char label[20], mne[20], opnd[20], addr[20], start_addr[20], optab_mne[20], optab_addr[20], symtab_mne[20], symtab_addr[20];
    int len;

    inp = fopen("input.txt", "r");
    optab = fopen("optab.txt", "r");
    symtab = fopen("symbol.txt", "r");
    flen = fopen("length.txt", "r");

    fscanf(inp, "%s%s%s%s", addr, label, mne, opnd);

    if(strcmp(mne, "START") == 0){
        strcpy(start_addr, opnd);
        fscanf(flen, "%d", &len);
    }

    printf("H^%s^%s^%d\n", label, opnd, len);
    printf("T^0000%s", opnd);

    fscanf(inp, "%s%s%s%s", addr, label, mne, opnd);
    while(strcmp(mne, "END") != 0){
        fscanf(optab, "%s%s", optab_mne, optab_addr);
        while(!feof(optab)){
            if(strcmp(mne, optab_mne) == 0){
                fclose(optab);
                fscanf(symtab, "%s%s", symtab_addr, symtab_mne);
                while(!feof(symtab)){
                    if(strcmp(opnd, symtab_mne) == 0){
                        fclose(symtab);
                        printf("%s%s^", optab_addr, symtab_addr);
                        break;   
                    }
                    fscanf(symtab, "%s%s", symtab_addr, symtab_mne);
                }
                break;
            }
            fscanf(optab, "%s%s", optab_mne, optab_addr);

        }
        if(strcmp(mne, "WORD") == 0 || strcmp(mne, "BYTE") == 0){
            if(strcmp(mne, "WORD") == 0){
                printf("0000%s^", opnd);
            }else{
                len = strlen(opnd);
                for(int i=2; i<len; i++){
                    printf("%s", opnd[i]);
                }
                printf("^");
            }
        }
        fscanf(inp, "%s%s%s%s", addr, label, mne, opnd);
        fseek(optab, SEEK_SET, 0);
    }
    
}