
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np
import csv


# with open('data/pmTest-Marker-3pic.csv') as file_obj: #test data 3 pic
# with open('data/pmTest1JUN2022-Marker.csv') as file_obj:  # rawData
# with open('data/testDemoScale2.csv') as file_obj:
#with open('data/testFix-data-plot.csv') as file_obj:
with open('data/oct-20-2022-00-05-data-plot.csv') as file_obj:
    reader_obj = csv.reader(file_obj)

    count = 0
    for row in reader_obj:

        fig = go.Figure(data=go.Contour(
            z=[
                [row[12], row[13], row[14], row[15]],
                [row[8], row[9], row[10], row[11]],
                [row[4], row[5], row[6], row[7]],
                [row[0], row[1], row[2], row[3]]
            ],
            # x=[0, 3], # horizontal axis
            # y=[0, 3], # vertical axis
            colorscale=[[0.000, "rgb(0,130,0)"],
                        [0.005, "rgb(0,140,0)"],
                        [0.010, "rgb(0,150,0)"],
                        [0.015, "rgb(0,160,0)"],
                        [0.020, "rgb(0,170,0)"],
                        [0.025, "rgb(0,180,0)"],
                        [0.030, "rgb(0,190,0)"],
                        [0.035, "rgb(0,200,0)"],
                        [0.040, "rgb(0,210,0)"],
                        [0.045, "rgb(0,220,0)"],
                        [0.050, "rgb(0,230,0)"],
                        [0.055, "rgb(0,240,0)"],
                        [0.060, "rgb(0,255,0)"],  # green
                        [0.065, "rgb(140,255,0)"],
                        [0.075, "rgb(160,255,0)"],
                        [0.085, "rgb(180,255,0)"],
                        [0.095, "rgb(200,255,0)"],
                        [0.105, "rgb(220,255,0)"],
                        [0.115, "rgb(240,255,0)"],
                        [0.125, "rgb(255,255,0)"],
                        [0.135, "rgb(255,240,0)"],
                        [0.145, "rgb(255,255,0)"],
                        [0.155, "rgb(255,210,0)"],
                        [0.165, "rgb(255,195,0)"],
                        [0.175, "rgb(255,180,0)"],  # Yellow
                        [0.220, "rgb(255,130,0)"],  # Orange
                        [0.275, "rgb(255,70,0)"],  # Orange
                        [0.525, "rgb(255,0,0)"],  # Red
                        [0.75, "rgb(150,0,0)"],  # Red
                        [0.85, "rgb(160,0,140)"],  # Purple
                        [1.0, "rgb(100,0,200)"]],  # Purple
            colorbar=dict(
                title="PM2.5 Level",
                titleside="top",
                tickmode="array",
                # tickvals=[0,12,35,50,150,250],
                #ticktext=["0","12", "35","55","150","250" ],
                ticks="outside"
            ),

            opacity=0.6,
            contours=dict(
                coloring='heatmap',
                showlabels=True,  # show labels on contours
                labelfont=dict(  # label font properties
                    size=8,
                    color='black',
                )
            )).update(zmin=0, zmax=200))  # Fix Color Scale Value

        

        fig.add_layout_image(
            dict(
                source="https://raw.githubusercontent.com/nitigan/heatMap/main/Map2.png",
                # source="/images/Map2.png",
                xref="x",
                yref="y",
                x=0,
                y=3,
                sizex=3,
                sizey=3,

                sizing="contain",  # ( "fill" | "contain" | "stretch" )
                opacity=1,
                layer="below")
        )
        '''
        #pin Station1
        fig.add_layout_image(
            dict(
                source="https://raw.githubusercontent.com/nitigan/heatMap/main/drop-pin.png",
                # source="/images/Map2.png",
                xref="x",
                yref="y",
                x=1.17,
                y=1.64,
                sizex=0.45,
                sizey=0.45,

                sizing="contain",  # ( "fill" | "contain" | "stretch" )
                opacity=0.5,
                layer="below"
                )
        )
        #pin Station2
        fig.add_layout_image(
            dict(
                source="https://raw.githubusercontent.com/nitigan/heatMap/main/drop-pin.png",
                # source="/images/Map2.png",
                xref="x",
                yref="y",
                x=1.65,
                y=2.28,
                sizex=0.45,
                sizey=0.45,

                sizing="contain",  # ( "fill" | "contain" | "stretch" )
                opacity=0.5,
                layer="below"
                )
        )
        
        #pin Station3
        fig.add_layout_image(
            dict(
                source="https://raw.githubusercontent.com/nitigan/heatMap/main/drop-pin.png",
                # source="/images/Map2.png",
                xref="x",
                yref="y",
                x=1.71,
                y=1.17,
                sizex=0.45,
                sizey=0.45,

                sizing="contain",  # ( "fill" | "contain" | "stretch" )
                opacity=0.5,
                layer="below"
                )
        )
        
        #pin Station4
        fig.add_layout_image(
            dict(
                source="https://raw.githubusercontent.com/nitigan/heatMap/main/drop-pin.png",
                # source="/images/Map2.png",
                xref="x",
                yref="y",
                x=2.78,
                y=1.90,
                sizex=0.45,
                sizey=0.45,

                sizing="contain",  # ( "fill" | "contain" | "stretch" )
                opacity=0.5,
                layer="below"
                )
        )
        #pin Station5
        fig.add_layout_image(
            dict(
                source="https://raw.githubusercontent.com/nitigan/heatMap/main/drop-pin.png",
                # source="/images/Map2.png",
                xref="x",
                yref="y",
                x=0.78,
                y=0.87,
                sizex=0.45,
                sizey=0.45,

                sizing="contain",  # ( "fill" | "contain" | "stretch" )
                opacity=0.5,
                layer="below"
                )
        )
        #pin Station6
        fig.add_layout_image(
            dict(
                source="https://raw.githubusercontent.com/nitigan/heatMap/main/drop-pin.png",
                # source="/images/Map2.png",
                xref="x",
                yref="y",
                x=1.03,
                y=3.00,
                sizex=0.45,
                sizey=0.45,

                sizing="contain",  # ( "fill" | "contain" | "stretch" )
                opacity=0.5,
                layer="below"
                )
        )
        #pin Station7
        fig.add_layout_image(
            dict(
                source="https://raw.githubusercontent.com/nitigan/heatMap/main/drop-pin.png",
                # source="/images/Map2.png",
                xref="x",
                yref="y",
                x=0.00,
                y=1.99,
                sizex=0.45,
                sizey=0.45,

                sizing="contain",  # ( "fill" | "contain" | "stretch" )
                opacity=0.5,
                layer="below"
                )
        )
        '''
        #PM Value 7 Station
        fig.add_trace(
            go.Scatter(
                mode='markers+text',

                # marker_symbol="triangle-down",

                # marker_coordinate
                x=[1.27, 1.75, 1.81, 2.88, 0.88, 1.13, 0.08],
                y=[1.51, 2.15, 1.04, 1.77, 0.74, 2.87, 1.86],
                marker=dict(
                    color='rgba(255, 0, 0, 0.7)',
                    size=40,
                    line=dict(
                        color='red',
                        width=1
                    ),

                ),
                text=[row[16], row[17], row[18],
                      row[19], row[20], row[21], row[22]],
                textposition="middle center",
                textfont=dict(
                    #family="sans serif",
                    size=12,
                    color="black"
                ),
                showlegend=False
            )
        )
        

        # PM Value 16 Point
        fig.add_trace(
            go.Scatter(
                #mode='markers+text',
                mode='text',

                # marker_symbol="triangle-down",

                # marker_coordinate
                x=[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3],
                y=[0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3],
                marker=dict(
                    color='rgba(255, 255, 255, 0.5)',
                    size=40,
                    line=dict(
                        color='rgba(255, 255, 255, 0.5)',
                        width=1
                    ),

                ),
                # Grid  Coordinate
                # [0,3][1,3][2,3][3,3]
                # [0,2][1,2][2,2][3,2]
                # [0,1][1,1][2,1][3,1]
                # [0,0][0,1][0,2][3,0]
                text=[row[12], row[8], row[4], row[0],
                      row[13], row[9], row[5], row[1],
                      row[14], row[10], row[6], row[2],
                      row[15], row[11], row[7], row[3]],
                textposition="middle center",
                textfont=dict(
                    #family="sans serif",
                    size=12,
                    color="black"
                ),
                showlegend=False
            )
        )

        # PM Value Marker Station 1
        fig.add_trace(
            go.Scatter(
                mode='markers+text',
                #marker_symbol="triangle-down",
                
                #mode='text',
                
                # marker_coordinate station1
                x=[1.27],
                y=[1.51],
                marker=dict(
                    color=[row[23]],
                    size=40,
                    line=dict(
                        color=[row[23]],
                        width=1
                    ),

                ),
                text=[row[16]],
                textposition="middle center",
                textfont=dict(
                    #family="sans serif",
                    size=15,
                    color="black"
                ),
                showlegend=False
            )
        )

        # PM Value Marker Station 2
        fig.add_trace(
            go.Scatter(
                mode='markers+text',
                #marker_symbol="triangle-down",
                
                #mode='text',

                # marker_coordinate station2
                x=[1.75],
                y=[2.15],
                marker=dict(
                    color=[row[24]],
                    size=40,
                    line=dict(
                        color=[row[24]],
                        width=1
                    ),

                ),
                text=[row[17]],
                textposition="middle center",
                textfont=dict(
                    #family="sans serif",
                    size=15,
                    color="black"
                ),
                showlegend=False
            )
        )

        # PM Value Marker Station 3
        fig.add_trace(
            go.Scatter(
                mode='markers+text',
                #marker_symbol="triangle-down",
                
                #mode='text',

                # marker_coordinate station2
                x=[1.81],
                y=[1.04],
                marker=dict(
                    color=[row[25]],
                    size=40,
                    line=dict(
                        color=[row[25]],
                        width=1
                    ),

                ),
                text=[row[18]],
                textposition="middle center",
                textfont=dict(
                    #family="sans serif",
                    size=15,
                    color="black"
                ),
                showlegend=False
            )
        )

        # PM Value Marker Station 4
        fig.add_trace(
            go.Scatter(
                mode='markers+text',
                #marker_symbol="triangle-down",
                
                #mode='text',

                # marker_coordinate station2
                x=[2.88],
                y=[1.77],
                marker=dict(
                    color=[row[26]],
                    size=40,
                    line=dict(
                        color=[row[26]],
                        width=1
                    ),

                ),
                text=[row[19]],
                textposition="middle center",
                textfont=dict(
                    #family="sans serif",
                    size=15,
                    color="black"
                ),
                showlegend=False
            )
        )

        # PM Value Marker Station 5
        fig.add_trace(
            go.Scatter(
                mode='markers+text',
                #marker_symbol="triangle-down",
                
                #mode='text',

                # marker_coordinate station2
                x=[0.88],
                y=[0.74],
                marker=dict(
                    color=[row[27]],
                    size=40,
                    line=dict(
                        color=[row[27]],
                        width=1
                    ),

                ),
                text=[row[20]],
                textposition="middle center",
                textfont=dict(
                    #family="sans serif",
                    size=15,
                    color="black"
                ),
                showlegend=False
            )
        )

        # PM Value Marker Station 6
        fig.add_trace(
            go.Scatter(
                mode='markers+text',
                #marker_symbol="triangle-down",
                
                #mode='text',

                # marker_coordinate station2
                x=[1.13],
                y=[2.87],
                marker=dict(
                    color=[row[28]],
                    size=40,
                    line=dict(
                        color=[row[28]],
                        width=1
                    ),

                ),
                text=[row[21]],
                textposition="middle center",
                textfont=dict(
                    #family="sans serif",
                    size=15,
                    color="black"
                ),
                showlegend=False
            )
        )

        # PM Value Marker Station 7
        fig.add_trace(
            go.Scatter(
                mode='markers+text',
                #marker_symbol="triangle-down",
                
                #mode='text',

                # marker_coordinate station2
                x=[0.08],
                y=[1.86],
                marker=dict(
                    color=[row[29]],
                    size=40,
                    line=dict(
                        color=[row[29]],
                        width=1
                    ),

                ),
                text=[row[22]],
                textposition="middle center",
                textfont=dict(
                    #family="sans serif",
                    size=15,
                    color="black"
                ),
                showlegend=False
            )
        )

        # StationLocation and DateTime
        fig.add_trace(
            go.Scatter(
                mode='text',

                # marker_symbol="triangle-down",

                # marker_coordinate
                x=[1.27, 1.75, 1.81, 2.88, 0.88, 1.13, 0.08, 2.50],
                y=[1.31, 1.95, 0.84, 1.57, 0.54, 2.67, 1.66, 3.00],
                # marker=dict(
                #    color='rgba(255, 0, 0, 0.7)',
                #    size=40,
                #    line=dict(
                #        color='red',
                #        width=1
                #    ),

                # ),
                text=["FITM", "WATER1", "ARGO",
                      "WATER3", "ENGINEER", "DORMITORY", "AIRPORT", row[30]],
                textposition="middle center",
                textfont=dict(
                    #family="sans serif",
                    size=12,
                    color="black"
                ),
                showlegend=False
            )
        )

        layout = go.Layout(template='none', width=400,
                           height=400, paper_bgcolor='black')
        if count < 10 :
            fig.write_image("images/4Nov-4Nov-circleMarker/00-triangle-00"+str(count) +
                        ".png", width=1000, height=655)
            count = count + 1
        elif count < 100 : 
            fig.write_image("images/4Nov-4Nov-circleMarker/00-triangle-0"+str(count) +
                        ".png", width=1000, height=655)
            count = count + 1
        else:
            # fig.write_image("images/testMaker/Marker"+str(count)+".png")
            fig.write_image("images/4Nov-4Nov-circleMarker/00-triangle-"+str(count) +
                            ".png", width=1000, height=655)
            count = count + 1

# display image in folder
import cv2
import glob

path = glob.glob("images/ColorScaleDemo10oct-22222/*.png")
# path = glob.glob("images/ShowPic/*.png") #showPic


for file in path:
    img = cv2.imread(file)

    cv2.imshow("Image", img)
    # cv2.waitKey(1000)
    cv2.waitKey(62)  # 16 frameper Second
