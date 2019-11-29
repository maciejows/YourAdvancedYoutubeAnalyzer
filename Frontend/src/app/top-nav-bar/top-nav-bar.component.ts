import { Component} from '@angular/core';

@Component({
  selector: 'app-top-nav-bar',
  templateUrl: './top-nav-bar.component.html',
  styleUrls: ['./top-nav-bar.component.scss']
})
export class TopNavBarComponent{

  options = ["Home", "About", "FAQ"];
  selectedOption: string = "Home";

  constructor() { }

  selectOption(option: string){
    this.selectedOption = option;
  }


}
