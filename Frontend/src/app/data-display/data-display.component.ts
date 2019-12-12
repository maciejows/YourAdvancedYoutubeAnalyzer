import { Component, Input} from '@angular/core';
import { Data } from '../data';

@Component({
  selector: 'app-data-display',
  templateUrl: './data-display.component.html',
  styleUrls: ['./data-display.component.scss']
})
export class DataDisplayComponent {

  @Input() data: Data;
  /* 
  data: Data = {
    ageLimit: 12,
    //Channel
    channelId: "channelId",
  	channelName: "channelName",
    channelPublishedAt: "channelPublishedAt",
    channelTotalVideoViews: "channelTotalVideoViews",
    channelUrl: "channelUrl",
    subscribersNumber: "subscribersNumber",
    videosNumber: "videosNumber", // ?
    //Video
    tags: ["asd", "dd"],
    thumbnailURL: "thumbnailURL",
    videoAverageRating: 12,
    videoCategories: ["asd", "dd"],
    videoDislikeCount: 12,
    videoDuration: 12,
    videoId: "videoId", // Ignore
    videoLikeCount: 12,
    videoTitle: "videoTitle",
    videoUploader: "videoUploader",
    videoUrl: "videoUrl", // Ignore
    videoViewCount: 12,
  }*/

  @Input() searched: boolean;
  
  options: string[] = ["Video", "Channel", "Additional"];
  selectedOption = "Video";

  constructor() { }

  selectOption(option: string): void{
    this.selectedOption = option;
  }
}
