import { Box, Grid2 } from "@mui/material";
import React, { Fragment } from "react";

interface params {
    data:any[]
}

export default function GuiList({data}:params) {
    return (
        <Fragment>
            <Box>
                <Grid2 container>
                    {data.map( item => <Fragment><Grid2 size={6}>{item.id}</Grid2><Grid2 size={6}>{item.risk}</Grid2></Fragment>)}
                </Grid2>
            </Box>
        </Fragment>
    )            
}