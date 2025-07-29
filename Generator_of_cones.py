#!/usr/bin/env python3
import numpy as np
from scipy.stats import boltzmann
import argparse
import os

def apply_fixed_zero_structure(A, zero_patterns):
    for row, cols in zero_patterns:
        for col in cols:
            A[row][col] = 0
    return A


def Cone(n, lambda_, N, f):
    filename = os.path.basename(f)
    
    # Define zeroing patterns based on file name
    zero_patterns = {
        "Cone9n_1.txt": [
            (0, [2, 3, 4, 5, 6, 7]),
            (1, [2, 3, 4, 5, 6]),
            (2, [1, 2, 3, 4, 5, 6]),
            (3, [1, 2, 3, 4, 5, 6]),
        ],
        "Cone9n_2.txt": [
            (0, [2, 3, 4, 5, 6, 7]),
            (1, [3, 4, 5, 6, 7, 8, 9]),
            (2, [3, 4, 5, 7, 8, 9]),
        ],
        "Cone9n_3.txt": [
            (0, [2, 3, 4, 5, 6, 7, 8, 9]),
            (1, [4, 5, 6, 7, 8 , 9]),
            (2, [0, 4, 5, 6, 7, 8, 9]),
        ], 
        "Cone9n_4.txt": [
            (0, [0, 4, 5, 6, 7, 8, 9]),
            (1, [0, 5, 6, 7, 8, 9]),
            (2, [0, 1, 5, 6, 7, 8, 9]),
        ],
        "Cone9n_5.txt": [
            (0, [0, 1, 5, 6, 7, 8, 9]),
            (1, [0, 1, 4, 6, 7, 8, 9]),
            (2, [0, 1, 2, 6, 7, 8, 9]),
        ],
        "Cone9n_6.txt": [
            (0, [0, 1, 2, 6, 7, 8, 9]),
            (1, [0, 1, 2, 7, 8, 9]),
            (2, [0, 1, 2, 3, 7, 8, 9]),
        ],
        "Cone9n_7.txt": [
            (0, [0, 1, 2, 3, 7, 8, 9]),
            (1, [0, 1, 2, 3, 8, 9]),
            (2, [0, 1, 2, 3, 4, 8, 9]),
        ],
        "Cone9n_8.txt": [
            (0, [0, 1, 2, 3, 4, 8, 9]),
            (1, [0, 1, 2, 3, 4, 9]),
            (2, [0, 1, 2, 3, 4, 5, 9]),
        ],
        "Cone9n_9.txt": [
            (0, [0, 1, 2, 3, 4, 5, 9]),
            (1, [1, 2, 3, 4, 5]),
            (2, [1, 2, 3, 4, 5, 6]),
        ],
        "Cone9n_10.txt": [
            (0, [1, 2, 3, 4, 5, 6]),
            (1, [1, 2, 3, 4, 5, 6]),
            (2, [1, 2, 3, 4, 5, 6]),
        ],
        "Cone8n_1.txt": [
            (0, [2, 3, 4, 5, 6]),
            (1, [2, 3, 4, 5]),
            (2, [1, 2, 3, 4, 5, 7]),
            (3, [1, 2, 3, 4, 5, 7]),
        ],
        "Cone8n_2.txt": [
            (0, [2, 3, 4, 5, 6, 7]),
            (1, [2, 3, 4, 5, 6, 7]),
            (2, [3, 4, 5, 6, 7]),
         ],
        "Cone8n_3.txt": [
            (0, [3, 4, 5, 6, 7]),
            (1, [4, 5, 6, 7]),
            (2, [0, 4, 5, 6, 7]),
         ],
        "Cone8n_4.txt": [
            (0, [0, 1, 5, 6, 7, 8]),
            (1, [0, 1, 6, 7, 8]),
            (2, [0, 1, 2, 6, 7, 8]),
         ],
        "Cone8n_5.txt": [
            (0, [0, 1, 2, 6, 7, 8]),
            (1, [0, 1, 2, 7, 8]),
            (2, [0, 1, 2, 3, 7, 8]),
         ],
        "Cone8n_5.txt": [
            (0, [0, 1, 2, 6, 7, 8]),
            (1, [0, 1, 2, 7, 8]),
            (2, [0, 1, 2, 3, 7, 8]),
         ],
        "Cone8n_6.txt": [
            (0, [0, 1, 2, 3, 7, 8]),
            (1, [0, 1, 2, 3, 8]),
            (2, [0, 1, 2, 3, 4, 8]),
         ],
        "Cone8n_7.txt": [
            (0, [0, 1, 2, 3, 4, 8]),
            (1, [0, 1, 2, 3, 4]),
            (2, [1, 2, 3, 4, 5]),
         ],
        "Cone8n_8.txt": [
            (0, [1, 2, 3, 4, 5]),
            (1, [1, 2, 3, 4, 5]),
            (2, [1, 2, 3, 4, 5, 6]),
         ],
        "Cone7n_1.txt": [
            (0, [2, 3, 4, 5]),
            (1, [2, 3, 4]),
            (2, [1, 2, 3, 4]),
            (3, [1, 2, 3, 4, 5]),
         ],
        "Cone7n_2.txt": [
            (0, [2, 3, 4, 5]),
            (1, [3, 4, 5]),
            (2, [3, 4, 5, 6, 7]),
         ],
        "Cone7n_3.txt": [
            (0, [3, 4, 5, 6, 7]),
            (1, [4, 5, 6, 7]),
            (2, [0, 4, 5, 6, 7]),
         ],
        "Cone7n_4.txt": [
            (0, [0, 2, 4, 5, 6, 7]),
            (1, [0, 4, 5, 6, 7]),
            (2, [0, 1, 5, 6, 7]),
         ],
        "Cone7n_5.txt": [
            (0, [0, 1, 5, 6, 7]),
            (1, [0, 1, 6, 7]),
            (2, [0, 1, 2, 6, 7]),
         ], 
        "Cone7n_6.txt": [
            (0, [0, 1, 2, 6, 7]),
            (1, [0, 1, 2, 7]),
            (2, [0, 1, 2, 3]),
         ],
        "Cone7n_7.txt": [
            (0, [0, 1, 2, 3]),
            (1, [1, 2, 3]),
            (2, [1, 2, 3, 4]),
         ], 
        "Cone7n_8.txt": [
            (0, [1, 2, 3, 4]),
            (1, [1, 2, 3, 4]),
            (2, [1, 2, 3, 4]),
         ],
        "Cone6n_1.txt": [
            (0, [2, 3, 4]),
            (1, [2, 3]),
            (2, [1, 2, 3]),
            (3, [1, 2, 3, 4]),
         ],
        "Cone6n_2.txt": [
            (0, [2, 3, 4]),
            (1, [3, 4]),
            (2, [3, 4, 5, 6]),
         ],
        "Cone6n_3.txt": [
            (0, [0, 4, 5, 6]),
            (1, [1, 5, 6]),
            (2, [0, 1, 5, 6]),
         ],
        "Cone6n_4.txt": [
            (0, [0, 1, 5, 6]),
            (1, [0, 1]),
            (2, [0, 1, 2]),
         ],
        "Cone6n_5.txt": [
            (0, [0, 1, 2]),
            (1, [1, 2]),
            (2, [1, 2, 3]),
         ],
        "Cone6n_6.txt": [
            (0, [1, 2, 3]),
            (1, [1, 2, 3]),
            (2, [1, 2, 3]),
         ],
        "Cone5n_1.txt": [
            (0, [2, 3]),
            (1, [2]),
            (2, [1, 2]),
            (3, [1, 2, 3]),
         ],
        "Cone5n_2.txt": [
            (0, [2, 3]),
            (1, [3]),
            (2, [3, 4, 5]),
         ],
        "Cone5n_3.txt": [
            (0, [3, 4, 5]),
            (1, [4, 5]),
            (2, [0, 4, 5]),
         ],
        "Cone5n_4.txt": [
            (0, [0, 4, 5]),
            (1, [0]),
            (2, [0, 1]),
         ],
        "Cone5n_5.txt": [
            (0, [0, 1]),
            (1, [1]),
            (2, [1, 2]),
         ],
        "Cone5n_6.txt": [
            (0, [1, 2]),
            (1, [1, 2]),
            (2, [1, 2]),
         ],
        "Cone4n_1.txt": [
            (0, [2]),
            (1, [2]),
            (2, [1]),
            (3, [1, 2]),
         ],
        "Cone4n_2.txt": [
            (0, [2]),
            (1, [3]),
            (2, [3, 4]),
         ],
        "Cone4n_3.txt": [
            (0, [3, 4]),
            (1, [4]),
            (2, [0, 4]),
         ],
        "Cone4n_4.txt": [
            (0, [0, 4]),
            (1, [0]),
            (2, [1]),
         ],
        "Cone4n_5.txt": [
            (0, [1]),
            (1, [1]),
            (2, [1, 2]),
         ],
        "Cone3n_1.txt": [
            (0, [2]),
            (1, [1]),
            (2, [1]),
            (3, [1]),
         ],
        "Cone3n_2.txt": [
            (0, [2]),
            (1, [3]),
            (2, [3]),
         ],
        "Cone3n_3.txt": [
            (0, [3]),
            (1, [0]),
            (2, [0]),
         ],
        "Cone3n_4.txt": [
            (0, [0]),
            (1, [0]),
            (2, [0, 1]),
         ]
        
    }

    base_output_name = "output"
    if  "9n_1" in filename:
        base_output_name = "TF_DNA91"
    elif "9n_2" in filename:
        base_output_name = "TF_DNA92"
    elif "9n_3" in filename:
        base_output_name = "TF_DNA93"
    elif "9n_4" in filename:
        base_output_name = "TF_DNA94"
    elif "9n_5" in filename:
        base_output_name = "TF_DNA95"
    elif "9n_6" in filename:
        base_output_name = "TF_DNA96"
    elif "9n_7" in filename:
        base_output_name = "TF_DNA97"
    elif "9n_8" in filename:
        base_output_name = "TF_DNA98"
    elif "9n_9" in filename:
        base_output_name = "TF_DNA99"
    elif "9n_10" in filename:
        base_output_name = "TF_DNA910"
    elif "8n_1" in filename:
        base_output_name = "TF_DNA81"    
    elif "8n_2" in filename:
        base_output_name = "TF_DNA82"
    elif "8n_3" in filename:
        base_output_name = "TF_DNA83"
    elif "8n_4" in filename:
        base_output_name = "TF_DNA84"
    elif "8n_5" in filename:
        base_output_name = "TF_DNA85"    
    elif "8n_6" in filename:
        base_output_name = "TF_DNA86"   
    elif "8n_7" in filename:
        base_output_name = "TF_DNA87"
    elif "8n_8" in filename:
        base_output_name = "TF_DNA88"
    elif "7n_1" in filename:
        base_output_name = "TF_DNA71"
    elif "7n_2" in filename:
        base_output_name = "TF_DNA72"
    elif "7n_3" in filename:
        base_output_name = "TF_DNA73"
    elif "7n_4" in filename:
        base_output_name = "TF_DNA74"
    elif "7n_5" in filename:
        base_output_name = "TF_DNA75"
    elif "7n_6" in filename:
        base_output_name = "TF_DNA76"
    elif "7n_7" in filename:
        base_output_name = "TF_DNA77"
    elif "7n_8" in filename:
        base_output_name = "TF_DNA78"
    elif "6n_1" in filename:
        base_output_name = "TF_DNA61"
    elif "6n_2" in filename:
        base_output_name = "TF_DNA62"
    elif "6n_3" in filename:
        base_output_name = "TF_DNA63"
    elif "6n_4" in filename:
        base_output_name = "TF_DNA64"
    elif "6n_5" in filename:
        base_output_name = "TF_DNA65"
    elif "6n_6" in filename:
        base_output_name = "TF_DNA66"
    elif "5n_1" in filename:
        base_output_name = "TF_DNA51"
    elif "5n_2" in filename:
        base_output_name = "TF_DNA52"
    elif "5n_3" in filename:
        base_output_name = "TF_DNA53"
    elif "5n_4" in filename:
        base_output_name = "TF_DNA54"
    elif "5n_5" in filename:
        base_output_name = "TF_DNA55"
    elif "5n_6" in filename:
        base_output_name = "TF_DNA56"
    elif "4n_1" in filename:
        base_output_name = "TF_DNA41"
    elif "4n_2" in filename:
        base_output_name = "TF_DNA42"
    elif "4n_3" in filename:
        base_output_name = "TF_DNA43"
    elif "4n_4" in filename:
        base_output_name = "TF_DNA44"
    elif "4n_5" in filename:
        base_output_name = "TF_DNA45"
    elif "3n_1" in filename:
        base_output_name = "TF_DNA31"
    elif "3n_2" in filename:
        base_output_name = "TF_DNA32"
    elif "3n_3" in filename:
        base_output_name = "TF_DNA33"
    elif "3n_4" in filename:
        base_output_name = "TF_DNA34"
    for r in range(1, n + 1):
        A = np.loadtxt(f)
        m, k = A.shape
        for j in range(m):
            for i in range(k):
                if A[j][i] == 0:
                    A[j][i] = boltzmann.rvs(lambda_, N, size=1)[0]
                else:
                    A[j][i] = 0  # overwrite non-zero with 0 as per original logic

        if filename in zero_patterns:
            A = apply_fixed_zero_structure(A, zero_patterns[filename])
            
        print(f"Matrix {r}:\n", A)
        
# Format matrix as: H1 = Matrix(ZZ, 4, 3, [...])
        matrix_flat_list = A.flatten().astype(int).tolist()
        matrix_str = f"H{r} = Matrix(ZZ, {A.shape[0]}, {A.shape[1]}, {matrix_flat_list})\n"
        #matrix_str = Matrix(ZZ, {A.shape[0]}, {A.shape[1]}, {matrix_flat_list})\n"
        #print(f"H{r}:\n")
# Save to file in SageMath matrix format
        #with open({base_output_name}.sage", 'w') as g:
        with open(f"{r}_{base_output_name}.sage", 'w') as g:
             g.write(matrix_str)


def main():
    parser = argparse.ArgumentParser(description="Generate random orthogonal matrices via Boltzmann distribution.")
    parser.add_argument('-n', type=int, default=10, help='Number of matrices to generate')
    parser.add_argument('--lambda_', type=float, default=1.5, help='Lambda parameter for Boltzmann distribution')
    parser.add_argument('-N', type=int, default=19, help='N parameter for Boltzmann distribution')
    parser.add_argument('-f', type=str, required=True, help='Path to input matrix file')
    #parser.add_argument('-m', type=int, default=4, help='Number of matrix rows')
    #parser.add_argument('-k', type=int, default=9, help='Number of matrix columns')
    
    args = parser.parse_args()
    Cone(args.n, args.lambda_, args.N, args.f)

if __name__ == '__main__':
    main()
