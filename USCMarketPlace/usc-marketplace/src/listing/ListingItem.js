import React from 'react';
import ImageList from '@mui/material/ImageList';
import ImageListItem from '@mui/material/ImageListItem';
import ImageListItemBar from '@mui/material/ImageListItemBar';
import ListSubheader from '@mui/material/ListSubheader';
import IconButton from '@mui/material/IconButton';
import InfoIcon from '@mui/icons-material/Info';
import { Link } from "react-router-dom";

const ListingItem = (props) => {
  return (
    <ImageListItem key={props.img}>
        <img
          src={`${props.img}`}
          srcSet={`${props.img}`}
          alt={props.title}
          //loading="lazy"
        />
        <ImageListItemBar
          title={props.title}
          subtitle={props.author}
          actionIcon={
            <IconButton
              sx={{ color: 'rgba(255, 255, 255, 0.54)' }}
              aria-label={`info about ${props.title}`}
            >
              {props.id &&
              <Link to={`/details/${props.id}`}>
                <InfoIcon />
              </Link>}
            </IconButton>
          }
        />
      </ImageListItem>
  );
}

export default ListingItem;