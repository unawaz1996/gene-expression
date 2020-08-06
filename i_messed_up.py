import os 

def get_list_of_files():
    """
    Input: Nothing 
    Output: Get a list of files in current directory

    """
    from os import listdir
    from os.path import isfile, join
    mypath = "."
    file_list = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    return file_list 


def get_gene_list(file_list):
    """
    Input: a list of files in this directory 
    Output: a list of gene names with no copies. 
    """
    gene_list = [] 
    for _file in file_list:
        if "ENSG" not in _file: continue 
        gene_list.append(_file.split("-")[0])
#    print(gene_list)
        
#    final_new_menu = list(set(new_menu))


    return list(set(gene_list))


#def format_subcaption(filename,gene):
#    """ 
#    Input: file
#    output: expression type 
#    """#
#
#    return filename.replace(gene,"")[1:].replace(".pdf","").replace("-expression","")




def output_latex_figure(file_list,gene_list):
    """
    Input : file_list and gene_list 
    
    """

    files = {}
    for gene in gene_list:
        files[gene] = []

    for gene in gene_list:
        for _file in list(set(file_list)):
            if gene not in _file: continue 
            files[gene].append(_file)

    for gene in gene_list:

        print(r"\begin{figure}[p]")
        print(r"\centering")
        i = 0 

        for _file in files[gene]:
            if gene not in _file: continue
            print(r"\begin{subfigure}[t]{0.49\textwidth}")
            print(r"\includegraphics[width=\textwidth]{%s}"%_file)
            print(r"\caption{\small{%s}}"%_file.replace(gene,"")[1:].replace(".pdf","").replace("-expression",""))
            print(r"\end{subfigure}")
            last_in_row = i%2 ==1
            not_the_last_file = (i+1 != len(files[gene] )) 
            
            if last_in_row and not_the_last_file: print(r"\\")

            i += 1

        print(r"\caption{%s}"%gene)
        print(r"\end{figure}")


#\begin{subfigure}[t]{0.49\textwidth}
#\includegraphics[width=\textwidth]{ENSG00000076685-MM-expression}
#\caption{Picture 2}
#\end{subfigure}


def main():


    file_list = get_list_of_files()    
    gene_list = get_gene_list(file_list)
    output_latex_figure(file_list,gene_list)


#for prefix in prefixlist:
#    print()




if __name__ == "__main__":
    main()

