import { Component, Input, OnChanges } from '@angular/core';
import {DomSanitizer} from '@angular/platform-browser';

@Component({
  selector: 'app-video-display',
  templateUrl: './video-display.component.html',
  styleUrls: ['./video-display.component.scss']
})
export class VideoDisplayComponent implements OnChanges{
  
  @Input() videoUrl: string;
  displayUrl: string;
  constructor(private domSanitizer: DomSanitizer) {}

  ngOnChanges(){
    console.log(this.videoUrl);
    this.displayUrl = `https://www.youtube.com/embed/${this.videoUrl.split('watch?v=')[1]}?controls=1`;
    console.log(this.displayUrl);
  }

  sanitizeUrl(){
    return this.domSanitizer.bypassSecurityTrustResourceUrl(this.displayUrl);
  }

}
