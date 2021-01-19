#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void main(){
    char label[20], mne[20], opnd[20], name[20], def_mne[20], def_opnd[20], arg[20];
    int len;
    FILE *inp, *argtab, *deftab, *namtab, *output;

    inp = fopen("inp.txt", "r");
    deftab = fopen("deftab.txt", "r");
    namtab = fopen("namtab.txt", "r");
    argtab = fopen("argtab.txt", "w+");
    output = fopen("output.txt", "w");

    fscanf(inp, "%s%s%s", label, mne, opnd);
    while(strcmp(mne, "END") != 0){
        if(strcmp(mne, "MACRO") ==0){
            fscanf(inp, "%s%s%s", label, mne, opnd);
            while(strcmp(mne, "MEND") != 0){
                fscanf(inp, "%s%s%s", label, mne, opnd);
            }
        }else{
            // check of this is macro invocation
            fscanf(namtab, "%s", name);
            if(strcmp(mne, name) == 0){

                // Enter Args into argtab
                len = strlen(opnd);
                for(int i=0; i<len; i++){
                    if(opnd[i] != ','){
                        fprintf(argtab, "%c", opnd[i]);
                    }else{
                        fprintf(argtab, "\n");
                    }
                }

                //reset argtab & namtab
                fseek(argtab, SEEK_SET, 0);
                fseek(namtab, SEEK_SET, 0);

                // write from deftab to output
                fscanf(deftab, "%s%s", def_mne, def_opnd);
                fprintf(output, "#\t%s\t%s\n", def_mne, opnd);
                fscanf(deftab, "%s%s", def_mne, def_opnd);
                while(strcmp(def_mne, "MEND") != 0){
                    if(def_opnd[0] == '&'){
                        fscanf(argtab, "%s", arg);
                        fprintf(output, "-\t%s\t%s\n", def_mne, arg);
                    }else{
                        fprintf(output, "-\t%s\t%s\n", def_mne, def_opnd);
                    }
                    fscanf(deftab, "%s%s", def_mne, def_opnd);
                }
            }else{
                fprintf(output, "%s\t%s\t%s\n", label, mne, opnd);
            }
        }
        fscanf(inp, "%s%s%s", label, mne, opnd);
    }
    fprintf(output, "%s\t%s\t%s\n", label, mne, opnd);
    fclose(inp);
    fclose(namtab);
    fclose(deftab);
    fclose(argtab);
    fclose(output);
    printf("pass is completed\n");
}