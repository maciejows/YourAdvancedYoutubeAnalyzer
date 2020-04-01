import { Component, Input, OnChanges } from '@angular/core';
import {DomSanitizer, SafeResourceUrl} from '@angular/platform-browser';


@Component({
  selector: 'app-video-display',
  templateUrl: './video-display.component.html',
  styleUrls: ['./video-display.component.scss']
})
export class VideoDisplayComponent implements OnChanges{
  
  @Input() videoUrl: string;
  sanitizedUrl: SafeResourceUrl;
  constructor(private domSanitizer: DomSanitizer) {}

  ngOnChanges(){
    this.sanitizeUrl();
  }

  sanitizeUrl(){
    this.sanitizedUrl = this.domSanitizer.bypassSecurityTrustResourceUrl(
      `https://www.youtube.com/embed/${this.videoUrl.split('watch?v=')[1]}?controls=1`
    );
  }

}