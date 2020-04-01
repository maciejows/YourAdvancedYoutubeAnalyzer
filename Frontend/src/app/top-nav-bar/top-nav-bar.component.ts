import { Component} from '@angular/core';
import { AppElementService } from '../services/app-element.service';

@Component({
  selector: 'app-top-nav-bar',
  templateUrl: './top-nav-bar.component.html',
  styleUrls: ['./top-nav-bar.component.scss']
})


export class TopNavBarComponent{

  options = ["Home", "About"];
  selectedOption: string = "Home";

  constructor(private appElementService: AppElementService) { }

  scrollToElement(option: string): void {
    this.appElementService.elements[option].scrollIntoView({behavior: "smooth", block: "center"});
  }

  selectOption(option: string){
    this.selectedOption = option;
    this.scrollToElement(option);
  }


}
