import { Component, Input, OnChanges } from '@angular/core';
import {DomSanitizer, SafeResourceUrl} from '@angular/platform-browser';
import { Data } from '../data';

@Component({
  selector: 'app-data-display',
  templateUrl: './data-display.component.html',
  styleUrls: ['./data-display.component.scss']
})
export class DataDisplayComponent implements OnChanges{

  @Input() data: Data;
  @Input() histogramUrl: string;
  @Input() searched: boolean;
  sanitizedUrl: SafeResourceUrl;

  options: string[] = ["Video", "Channel", "Additional"];
  selectedOption = "Video";

  constructor(private domSanitizer: DomSanitizer) { }

  ngOnChanges(){
    this.sanitizeUrl();
  }

  sanitizeUrl(){
    this.sanitizedUrl = this.domSanitizer.bypassSecurityTrustResourceUrl(this.histogramUrl);
  }

  selectOption(option: string): void{
    this.selectedOption = option;
  }
}
