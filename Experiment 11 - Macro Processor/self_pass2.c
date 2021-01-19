#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void main(){
    int len;
    char label[20], mne[20], opnd[20], name[20], mne1[20], opnd1[20], arg[20];
    FILE *inp, *argtab, *deftab, *namtab, *output;
    inp = fopen("inp_self.txt", "r");
    argtab = fopen("argtab.txt", "w+");
    deftab = fopen("deftab_self.txt", "r");
    namtab = fopen("namtab_self.txt", "r");
    output = fopen("output_self.txt", "w");

    fscanf(inp , "%s%s%s", label, mne, opnd);
    
    while(strcmp("END", mne) != 0){
        if(strcmp(mne, "MACRO") == 0){
            fscanf(inp , "%s%s%s", label, mne, opnd);
            while(strcmp(mne, "MEND") != 0){
                fscanf(inp , "%s%s%s", label, mne, opnd);
            } 
        }else{
            fscanf(namtab, "%s", name);
            if(strcmp(mne, name) == 0){
                // taking length of args
                // Storing args in argtab
                len = strlen(opnd);
                for(int i=0; i<len; i++){
                    if(opnd[i] != ','){
                        fprintf(argtab, "%c", opnd[i]);
                    }else{
                        fprintf(argtab, "\n");
                    }
                }

                fseek(namtab, SEEK_SET, 0);
                fseek(argtab, SEEK_SET, 0);

                // writing from deftab to output
                fscanf(deftab, "%s%s", mne1, opnd1);
                fprintf(output, ".\t%s\t%s\n", mne1, opnd);
                fscanf(deftab, "%s%s", mne1, opnd1);
                while(strcmp(mne1, "MEND") != 0){
                    if(opnd1[0] == '&'){
                        fscanf(argtab, "%s", arg);
                        fprintf(output, "-\t%s\t%s\n", mne1, arg);
                    }else{
                        fprintf(output, "-\t%s\t%s\n", mne1, opnd1);
                    }
                    fscanf(deftab, "%s%s", mne1, opnd1);

                } 
            }else{
                fprintf(output, "%s\t%s\t%s\n", label, mne, opnd);
            }
        }
        fscanf(inp , "%s%s%s", label, mne, opnd);
    }
    fprintf(output, "%s\t%s\t%s\n", label, mne, opnd);
    fclose(inp);
    fclose(argtab);
    fclose(namtab);
    fclose(deftab);
    fclose(output);
    printf("Pass 2 complete\n");
}