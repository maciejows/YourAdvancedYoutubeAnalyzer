import { Component, ViewChild, ElementRef, AfterViewInit} from '@angular/core';
import { Data } from './data';
import { AppElementService } from './services/app-element.service'
import { AboutComponent } from './about/about.component';
import { SearchBarComponent } from './search-bar/search-bar.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements AfterViewInit {
  @ViewChild(AboutComponent, {read: ElementRef, static: true}) aboutElementRef: ElementRef;
  @ViewChild(SearchBarComponent, {read: ElementRef, static: true}) homeElementRef: ElementRef; // Reference to Search bar for scroll purposes

  data: Data;
  histogramUrl: any;
  searched: boolean;
  
  constructor(private appElementsService: AppElementService) { }

  ngAfterViewInit(){
    this.appElementsService.elements["About"] = this.aboutElementRef.nativeElement;
    this.appElementsService.elements["Home"] = this.homeElementRef.nativeElement;
  }

  getData(event: Data){
    this.data = event;
    console.log("Got data in app.component");
  }

  getHistogram(event: any){
    this.histogramUrl = event;
    console.log("Got histogram in app.component");
  }

  isSearching(event: boolean){
    this.searched = event;
  }

}
