import { Component } from '@angular/core';
import { AppElementService } from '../services/app-element.service';

@Component({
  selector: 'app-bottom-nav-bar',
  templateUrl: './bottom-nav-bar.component.html',
  styleUrls: ['./bottom-nav-bar.component.scss']
})
export class BottomNavBarComponent {

  options = ["Home", "About"];

  constructor(private appElementService: AppElementService) { }

  scrollToElement(option: string): void {
    this.appElementService.elements[option].scrollIntoView({behavior: "smooth", block: "center"});
  }

  selectOption(option: string){
    this.scrollToElement(option);
  }

}
