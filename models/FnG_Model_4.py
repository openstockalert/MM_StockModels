import pandas as pd
import matplotlib.pyplot as plt

import numpy as np

def plot_sp500_data(sp500_percentages, sp500_means, sp500_stds):
    # Create a figure and axis
    fig, ax = plt.subplots(1, 3, figsize=(18, 6))

    # Plot data
    ax[0].bar(range(len(sp500_percentages)), sp500_percentages)
    ax[1].bar(range(len(sp500_means)), sp500_means)
    ax[2].bar(range(len(sp500_stds)), sp500_stds)

    # Set titles and labels
    ax[0].set_title('S&P 500 Percentages')
    ax[0].set_xlabel('Time Period')
    ax[0].set_ylabel('Percentage')
    ax[0].set_xticks(range(len(sp500_percentages)))
    ax[0].set_xticklabels(['1 day', '3 days', '5 days', '14 days', '28 days'])

    ax[1].set_title('S&P 500 Means')
    ax[1].set_xlabel('Time Period')
    ax[1].set_ylabel('Mean')
    ax[1].set_xticks(range(len(sp500_means)))
    ax[1].set_xticklabels(['1 day', '3 days', '5 days', '14 days', '28 days'])

    ax[2].set_title('S&P 500 Standard Deviations')
    ax[2].set_xlabel('Time Period')
    ax[2].set_ylabel('Standard Deviation')
    ax[2].set_xticks(range(len(sp500_stds)))
    ax[2].set_xticklabels(['1 day', '3 days', '5 days', '14 days', '28 days'])

    # Show plot
    plt.tight_layout()
    plt.show()


import matplotlib.pyplot as plt

def plot_sp500_data2(sp500_percentages, sp500_means, sp500_stds):
    # Create a figure and axis
    fig, ax = plt.subplots(1, 3, figsize=(18, 6))

    # Plot data
    ax[0].bar(range(len(sp500_percentages[0])), sp500_percentages[0], label='Set 1')
    ax[0].bar(range(len(sp500_percentages[0])), sp500_percentages[1], bottom=sp500_percentages[0], label='Set 2')
    ax[1].bar(range(len(sp500_means[0])), sp500_means[0], label='Set 1')
    ax[1].bar(range(len(sp500_means[0])), sp500_means[1], bottom=sp500_means[0], label='Set 2')
    ax[2].bar(range(len(sp500_stds[0])), sp500_stds[0], label='Set 1')
    ax[2].bar(range(len(sp500_stds[0])), sp500_stds[1], bottom=sp500_stds[0], label='Set 2')

    # Set titles and labels
    ax[0].set_title('S&P 500 Percentages')
    ax[0].set_xlabel('Time Period')
    ax[0].set_ylabel('Percentage')
    ax[0].set_xticks(range(len(sp500_percentages[0])))
    ax[0].set_xticklabels(['1 day', '3 days', '5 days', '14 days', '28 days'])

    ax[1].set_title('S&P 500 Means')
    ax[1].set_xlabel('Time Period')
    ax[1].set_ylabel('Mean')
    ax[1].set_xticks(range(len(sp500_means[0])))
    ax[1].set_xticklabels(['1 day', '3 days', '5 days', '14 days', '28 days'])

    ax[2].set_title('S&P 500 Standard Deviations')
    ax[2].set_xlabel('Time Period')
    ax[2].set_ylabel('Standard Deviation')
    ax[2].set_xticks(range(len(sp500_stds[0])))
    ax[2].set_xticklabels(['1 day', '3 days', '5 days', '14 days', '28 days'])

    # Add legend
    ax[0].legend()
    ax[1].legend()
    ax[2].legend()

    # Show plot
    plt.tight_layout()
    plt.show()


def plot_sp500_data_comparison(sp500_percentages, sp500_means, sp500_stds, chart_name):
    # Create a figure and axis
    fig, ax = plt.subplots(1, 3, figsize=(18, 6))

    # Define the x-axis values
    x = np.arange(len(sp500_percentages[0]))
    width = 0.35

    set1 = "Control"
    set2 = "Model"
    # Plot data
    ax[0].bar(x - width/2, sp500_percentages[0], width, label=set1)
    ax[0].bar(x + width/2, sp500_percentages[1], width, label=set2)
    ax[1].bar(x - width/2, sp500_means[0], width, label=set1)
    ax[1].bar(x + width/2, sp500_means[1], width, label=set2)
    ax[2].bar(x - width/2, sp500_stds[0], width, label=set1)
    ax[2].bar(x + width/2, sp500_stds[1], width, label=set2)

    # Set titles and labels
    ax[0].set_title('S&P500 Index Up Days/Total Days(%)')
    ax[0].set_xlabel('Time Period')
    ax[0].set_ylabel('Percentage')
    ax[0].set_xticks(x)
    ax[0].set_xticklabels(['1 day', '3 days', '5 days', '14 days', '28 days'])

    ax[1].set_title('S&P500 Index Change Percentage - Mean')
    ax[1].set_xlabel('Time Period')
    ax[1].set_ylabel('Mean')
    ax[1].set_xticks(x)
    ax[1].set_xticklabels(['1 day', '3 days', '5 days', '14 days', '28 days'])

    ax[2].set_title('S&P500 Change Percentage - Standard Deviations')
    ax[2].set_xlabel('Time Period')
    ax[2].set_ylabel('Standard Deviation')
    ax[2].set_xticks(x)
    ax[2].set_xticklabels(['1 day', '3 days', '5 days', '14 days', '28 days'])

    # Add horizontal grid lines
    ax[0].grid(axis='y', linestyle='--', alpha=0.7)
    ax[1].grid(axis='y', linestyle='--', alpha=0.7)
    ax[2].grid(axis='y', linestyle='--', alpha=0.7)

    # Add legend
    ax[0].legend()
    ax[1].legend()
    ax[2].legend()

    # plt.ion()
    # Show plot
    plt.suptitle(f"Chart {chart_name}")
    plt.tight_layout()
    plt.show()



def print_sp500_stats(df, name, sample_size=2443):
    model_selected_count = len(df)
    fng_avg = df['FNG'].mean().round(2)
    fng_dev = df['FNG'].std().round(2)
    SP500_Change_1day_mean = df['SP500_Change_1day'].mean().round(2)
    SP500_Change_1day_std = df['SP500_Change_1day'].std().round(2)
    SP500_Change_3day_mean = df['SP500_Change_3day'].mean().round(2)
    SP500_Change_3day_std = df['SP500_Change_3day'].std().round(2)
    SP500_Change_5day_mean = df['SP500_Change_5day'].mean().round(2)
    SP500_Change_5day_std = df['SP500_Change_5day'].std().round(2)
    SP500_Change_14day_mean = df['SP500_Change_14day'].mean().round(2)
    SP500_Change_14day_std = df['SP500_Change_14day'].std().round(2)
    SP500_Change_28day_mean = df['SP500_Change_28day'].mean().round(2)
    SP500_Change_28day_std = df['SP500_Change_28day'].std().round(2)
    sp500_sum_1day = df['S&P_1day_up'].sum()
    sp500_percentage_1day = (sp500_sum_1day / model_selected_count) * 100
    sp500_sum_3day = df['S&P_3day_up'].sum()
    sp500_percentage_3day = (sp500_sum_3day / model_selected_count) * 100    
    sp500_sum_5day = df['S&P_5day_up'].sum()        
    sp500_percentage_5day = (sp500_sum_5day / model_selected_count) * 100        
    sp500_sum_14day = df['S&P_14day_up'].sum()                
    sp500_percentage_14day = (sp500_sum_14day / model_selected_count) * 100                
    sp500_sum_28day = df['S&P_28day_up'].sum()                        
    sp500_percentage_28day = (sp500_sum_28day / model_selected_count) * 100



    
    with open("models/results/output.txt", "a") as f:
        f.write(f"Dataframe: {name}\n")
        f.write(f"Total Sample Count: {sample_size}\n")
        f.write(f"Model Selected Count: {model_selected_count}\n")
        f.write(f"Sample Percentage: {model_selected_count / sample_size * 100:.2f}%\n")
        f.write(f"Sum of S&P_1day_up: {sp500_sum_1day}\n")
        f.write(f"Percentage of S&P_1day_up: {sp500_percentage_1day:.2f}%\n")
        f.write(f"Mean of SP500_Change_1day: {SP500_Change_1day_mean}\n")
        f.write(f"Std Dev of SP500_Change_1day: {SP500_Change_1day_std}\n")
        f.write(f"Sum of S&P_3day_up: {sp500_sum_3day}\n")
        f.write(f"Percentage of S&P_3day_up: {sp500_percentage_3day:.2f}%\n")
        f.write(f"Mean of SP500_Change_3day: {SP500_Change_3day_mean}\n")
        f.write(f"Std Dev of SP500_Change_3day: {SP500_Change_3day_std}\n")
        f.write(f"Sum of S&P_5day_up: {sp500_sum_5day}\n")
        f.write(f"Percentage of S&P_5day_up: {sp500_percentage_5day:.2f}%\n")
        f.write(f"Mean of SP500_Change_5day: {SP500_Change_5day_mean}\n")
        f.write(f"Std Dev of SP500_Change_5day: {SP500_Change_5day_std}\n")
        f.write(f"Sum of S&P_14day_up: {sp500_sum_14day}\n")
        f.write(f"Percentage of S&P_14day_up: {sp500_percentage_14day:.2f}%\n")
        f.write(f"Mean of SP500_Change_14day: {SP500_Change_14day_mean}\n")
        f.write(f"Std Dev of SP500_Change_14day: {SP500_Change_14day_std}\n")
        f.write(f"Sum of S&P_28day_up: {sp500_sum_28day}\n")
        f.write(f"Percentage of S&P_28day_up: {sp500_percentage_28day:.2f}%\n")
        f.write(f"Mean of SP500_Change_28day: {SP500_Change_28day_mean}\n")
        f.write(f"Std Dev of SP500_Change_28day: {SP500_Change_28day_std}\n")
        f.write(f"Mean of FNG: {fng_avg}\n")
        f.write(f"Std Dev of FNG: {fng_dev}\n")
        f.write("---------------------------\n")
        f.write("\n")


    #sp500_sums = [sp500_sum_1day, sp500_sum_3day, sp500_sum_5day, sp500_sum_14day, sp500_sum_28day]
    sp500_percentages = [sp500_percentage_1day, sp500_percentage_3day, sp500_percentage_5day, sp500_percentage_14day, sp500_percentage_28day]
    sp500_means = [SP500_Change_1day_mean, SP500_Change_3day_mean, SP500_Change_5day_mean, SP500_Change_14day_mean, SP500_Change_28day_mean]
    sp500_stds = [SP500_Change_1day_std, SP500_Change_3day_std, SP500_Change_5day_std, SP500_Change_14day_std, SP500_Change_28day_std]

    return sp500_percentages, sp500_means, sp500_stds


# Load the data
data = pd.read_csv('features/processed_data/feature_data_sp_change4.csv')

# for chart data
sp500_percentages = []
sp500_means = []
sp500_stds = []


#sp_change_range = range(-20, 1)
#sp_change_range = np.arange(-0.09, -0.16, -0.02)
sp_change_range = np.arange(-0.01, -0.2, -0.01)
fn_change_range = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
#fn_change_range = [0, 0.5, 1.0]


p1, p2, p3 = print_sp500_stats(data, "total samples")


for sp_change in sp_change_range:
    sp_change = sp_change.round(2)
    result = data[(data['SP500_Change_Percentage'] < sp_change)]
    result.to_csv(f"models/results/sp_change_{sp_change}.csv", index=False)
    print_sp500_stats(result, f"sp_change: {sp_change}")
    for fn_change in fn_change_range:
        sp500_percentages.append(p1)
        sp500_means.append(p2)
        sp500_stds.append(p3)

        result = data[(data['SP500_Change_Percentage'] < sp_change) & (data['FNG_Change'] > fn_change)]
        result.to_csv(f"models/results/sp_change_{sp_change}_fn_change_{fn_change}.csv", index=False)
        chart_name = f"sp_change: {sp_change}, fn_change: {fn_change}"
        r1, r2, r3 = print_sp500_stats(result, f"{chart_name}")
        print(f"{chart_name}")
        
        sp500_percentages.append(r1)
        sp500_means.append(r2)
        sp500_stds.append(r3)


        # if sp_change == -0.11 and fn_change == 0.5:
        # plot_sp500_data_comparison(sp500_percentages, sp500_means, sp500_stds, chart_name)



# for fn_change in fn_change_range:
#     result = data[(data['FNG_Change'] > fn_change)]
#     print_sp500_stats(result, f"FNG_Change: {fn_change}")
#     for sp_change in sp_change_range:
#         result = data[(data['SP500_Change'] < sp_change) & (data['FNG_Change'] > fn_change)]
#         print_sp500_stats(result, f"sp_change: {sp_change}, fn_change: {fn_change}")



print("Done.")